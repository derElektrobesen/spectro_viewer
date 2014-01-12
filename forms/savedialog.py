from PyQt4.QtGui import QMainWindow, QMessageBox, QCompleter
from PyQt4.QtCore import QObject, pyqtSlot, SIGNAL, Qt
from PyQt4.QtSql import QSqlQuery
from pr_core import translate
from db import DB
import re
from settings import Settings
from .save_dialog import Ui_MainWindow as Ui_SaveDialog
from .extrainfowindow import ExtraInfoWindow

class ReqType:
    select_cards = 0
    select_names = 1

class SaveDialog(QMainWindow, Ui_SaveDialog):
    def __init__(self, parent = None, collection = None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.__collection = collection
        self.__do_text_search = True
        self.__visit_id = 0
        self.__names = {}

        self.set_measure_box_value()

        self.connect_slots()
        self.set_completers()
        self.prepare_queries()

    def connect_slots(self):
        QObject.connect(self.measures_box, SIGNAL("currentIndexChanged(int)"), self.on_index_changed)

    def prepare_queries(self):
        def f(q):
            s = QSqlQuery(DB.con())
            s.prepare(q)
            return s

        self.__queries = {
            'add_visit':    f('select add_visit(?)'),
            'add_graph':    f('select add_graph(?, ?, ?, ?)'),
            'add_point':    f('insert into Data(diagram_id, point) values (?, POINT(?, ?))'),
            'have_intact':  f('select have_intact(?)'),
        }

    def set_collection(self, collection):
        self.__collection = collection

    def set_measure_box_value(self):
        self.measures_box.clear()

        if not self.__collection:
            return

        m_format_str = translate("Measure", "Измерение") + ": %d"
        format_str = m_format_str + ", " + \
                translate("Spectr", "Спектр") + ": %d"
        for i, measure in enumerate(self.__collection):
            if measure.count() == 1:
                self.measures_box.addItem(m_format_str % (i + 1), { 'measure': i, 'graph': 0 })
            else:
                for j in range(measure.count()):
                    self.measures_box.addItem(format_str % (i + 1, j + 1), { 'measure': i, 'graph': j })

        self.on_index_changed(0)

    def set_progress(self, val, pr_range = (0,100)):
        self.progressBar.setMinimum(pr_range[0])
        self.progressBar.setMaximum(pr_range[1])
        self.progressBar.setValue(val)

    def set_completers(self):
        c = QCompleter(self.get_names_list(), self)
        c.setCaseSensitivity(Qt.CaseInsensitive)
        self.name_edt.setCompleter(c)

    def get_names_list(self):
        q = QSqlQuery(DB.con())
        q.prepare("call select_names()")
        q.exec_()
        q.prepare("select lastname, name, middlename, card_no, id from filtered_names")
        q.exec_()
        r = []
        while (q.next()):
            t = q.value(0) + " " + q.value(1) + " " + q.value(2)
            r.append(t)
            self.__names[t.lower()] = {'card': q.value(3), 'id': q.value(4),}
        return r

    def save_graph(self, cli_id, text, is_intact):
        q = self.__queries['add_visit']
        q.bindValue(0, cli_id)
        q.exec_()
        q.next()
        visit_id = q.value(0)
        q.finish()

        q = self.__queries['have_intact']
        q.bindValue(0, visit_id)
        q.exec_()
        r = q.value(0)
        q.finish()

        if r:
            QMessageBox.critical(self, translate("Error", "Ошибка"),
                    translate("Intact_already_exists", "Интактная точка уже была сохранена. Изменить интактную " +
                        "точку можно в истории посещений больного."))
            return visit_id

        index = self.get_indexes()
        gr = self.__collection.get_measure(index['measure']).get_graph(index['graph'])

        DB.con().transaction()
        q = self.__queries['add_graph']
        q.bindValue(0, visit_id)
        q.bindValue(1, Settings.device_type)
        q.bindValue(2, text)
        q.bindValue(3, 'intact' if is_intact else 'other')
        q.exec_()
        q.next()
        gr_id = q.value(0)
        q.finish()
        q = self.__queries['add_point']

        l = len(gr)
        self.set_progress(0, (0, l))
        i = 0
        for x, y in gr:
            i += 1
            q.bindValue(0, gr_id)
            q.bindValue(1, x)
            q.bindValue(2, y)
            q.exec_()
            q.finish()
            if i % 200 == 0:
                self.set_progress(i, (0, l))
        self.set_progress(100)

        DB.con().commit()

        return visit_id

    def save_extra_info(self):
        if self.__visit_id:
            wnd = ExtraInfoWindow(self, self.__visit_id)
            wnd.show()
        self.close()

    @pyqtSlot()
    def on_remove_measure_btn_clicked(self):
        self.set_progress(0)
        if self.measures_box.count() > 1:
            i = self.measures_box.currentIndex()
            index = self.measures_box.itemData(i)
            self.__collection.get_measure(index['measure']).remove_graph_deffered(index['graph'])
            self.measures_box.removeItem(i)
        if self.measures_box.count() == 1:
            self.remove_measure_btn.setEnabled(False)
        self.set_progress(100)

    def get_indexes(self, index = -1):
        if index < 0:
            index = self.measures_box.currentIndex()
        return self.measures_box.itemData(index)

    @pyqtSlot()
    def on_average_btn_clicked(self):
        self.set_progress(0)
        index = self.get_indexes()
        if index:
            measure = self.__collection.get_measure(index['measure'])
            measure = measure.remove_deffered_graphs().average_graphs()
            self.__collection.set_measure(index['measure'], measure)
            self.set_measure_box_value()
        self.set_progress(100)

    @pyqtSlot(int)
    def on_index_changed(self, index):
        index = self.get_indexes(index)
        if index:
            gr = self.__collection.get_measure(index['measure']).get_graph(index['graph'])
            self.cur_measure_wgt.set_graph("{measure}-{graph}".format(**index), gr)
            self.cur_measure_wgt.render()

    def incorrect_user(self):
        QMessageBox.critical(self, translate("Error", "Ошибка"),
                translate("Names_err", "Введены некорректные данные о пациенте (имя и/или номер карты)."))
    def incorrect_pnt(self):
        QMessageBox.critical(self, translate("Error", "Ошибка"),
                translate("Point_err", "Вверено некорректное название точки"))

    @pyqtSlot()
    def on_save_btn_clicked(self):
        return self.do_save(False)

    @pyqtSlot()
    def on_save_intact_btn_clicked(self):
        return self.do_save(True)

    def do_save(self, is_intact):
        text = self.name_edt.text().lower()
        if text not in self.__names:
            return self.incorrect_user()
        cli_id = self.__names[text]['id']
        text = self.pnt_edt.text().strip()
        if not len(text):
            return self.incorrect_pnt()
        self.__visit_id = self.save_graph(cli_id, text, is_intact)
        
    @pyqtSlot()
    def on_close_btn_pressed(self):
        self.save_extra_info()

    @pyqtSlot()
    def on_name_edt_editingFinished(self):
        text = self.name_edt.text().lower()
        if text in self.__names:
            self.card_no_edt.setText(self.__names[text]['card'])
        else:
            self.card_no_edt.clear()
