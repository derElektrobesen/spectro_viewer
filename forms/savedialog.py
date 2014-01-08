from PyQt4.QtGui import QMainWindow, QStandardItemModel, QStandardItem, QMessageBox
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

class CompleterText:
    def __init__(self, parent = None):
        self.__req = None
        self.__select = QSqlQuery(DB.con())
        self.__select.prepare("select id, lastname, name, middlename, card_no from filtered_names")
        self.__data = None

    def update_data(self, text):
        if self.__req:
            p = re.compile('\s+')
            p.sub(text, ' ')
            self.__req.bindValue(0, text)
            self.__req.exec_()
            self.__req.finish()

            self.__rows = []

            q = self.__select
            q.exec_()
            if q.next():
                self.__data = {
                    'id': q.value(0),
                    'lastname': q.value(1),
                    'name': q.value(2),
                    'middlename': q.value(3),
                    'card': q.value(4),
                }
                self.set_text()
            else:
                self.__data = None
            q.finish()

    def set_text(self):
        items = ['lastname', 'name', 'middlename'] if self.__req_type == ReqType.select_names else ['card']
        text = ''
        for key in items:
            text += self.__data[key] + " "
        self.__data['text'] = text[:-1]

    def set_request(self, req_type):
        self.__req = QSqlQuery(DB.con())
        text = None
        if req_type == ReqType.select_cards:
            text = 'call search_card(?)'
            self.__keys = ['lastname', 'name', 'middlename']
        elif req_type == ReqType.select_names:
            text = 'call search_name(?)'
            self.__keys = ['card']
        if text:
            self.__req.prepare(text)
            self.__req_type = req_type

    def get_text(self):
        return self.__data and self.__data['text']

    def get_id(self):
        return self.__data and self.__data['id']

    def get_other_text(self):
        t = ''
        if self.__data:
            for key in self.__keys:
                t += self.__data[key] + " "
            t = t[:-1]
        return t

    def get_data(self):
        return self.__data

class SaveDialog(QMainWindow, Ui_SaveDialog):
    def __init__(self, parent = None, collection = None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.__collection = collection
        self.__do_text_search = True
        self.__visit_id = 0

        self.set_measure_box_value()

        self.connect_slots()
        self.set_completers()
        self.prepare_queries()

    def connect_slots(self):
        QObject.connect(self.measures_box, SIGNAL("currentIndexChanged(int)"), self.on_index_changed)
        QObject.connect(self.name_edt, SIGNAL("textChanged(QString)"), self.on_main_text_changed)
        QObject.connect(self.card_no_edt, SIGNAL("textChanged(QString)"), self.on_main_text_changed)

    def prepare_queries(self):
        def f(q):
            s = QSqlQuery(DB.con())
            s.prepare(q)
            return s

        self.__queries = {
            'add_visit':    f('select add_visit(?)'),
            'add_graph':    f('select add_graph(?, ?, ?)'),
            'add_point':    f('insert into Data(diagram_id, point) values (?, POINT(?, ?))')
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
        m = CompleterText()
        m.set_request(ReqType.select_names)
        self.name_edt_lines = m

        m = CompleterText()
        m.set_request(ReqType.select_cards)
        self.card_no_lines = m

    def save_graph(self, cli_id, text):
        q = self.__queries['add_visit']
        q.bindValue(0, cli_id)
        q.exec_()
        q.next()
        visit_id = q.value(0)
        q.finish()

        index = self.get_indexes()
        gr = self.__collection.get_measure(index['measure']).get_graph(index['graph'])

        DB.con().transaction()
        q = self.__queries['add_graph']
        q.bindValue(0, visit_id)
        q.bindValue(1, Settings.device_type)
        q.bindValue(2, text)
        q.exec_()
        q.next()
        gr_id = q.value(0)
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
        wnd = ExtraInfoWindow(self, self.__visit_id)
        wnd.show()

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

    @pyqtSlot('QString')
    def on_main_text_changed(self, text):
        if not self.__do_text_search:
            self.__do_text_search = True
            return

        edt = self.sender()
        if edt.is_backspace_pressed():
            return

        ref = {
            'name_edt': self.name_edt_lines,
            'card_no_edt': self.card_no_lines,
        }.get(self.sender().objectName(), None)
        other = self.name_edt if ref == self.card_no_lines else self.card_no_edt
        if ref:
            ref.update_data(text)
            t = ref.get_text()
            if t:
                self.__do_text_search = False
                other.setText(ref.get_other_text())
                edt.setText(t)
                edt.setSelection(len(text), len(t) - len(text))

    def incorrect_user(self):
        QMessageBox.critical(self, translate("Error", "Ошибка"),
                translate("Names_err", "Введены некорректные данные о пациенте (имя и/или номер карты)."))
    def incorrect_pnt(self):
        QMessageBox.critical(self, translate("Error", "Ошибка"),
                translate("Point_err", "Вверено некорректное название точки"))

    @pyqtSlot()
    def on_save_btn_clicked(self):
        cli_id = None
        for confirmator, edt in (
                (self.name_edt_lines, self.name_edt),
                (self.card_no_lines, self.card_no_edt)):
            if len(edt.text()) == 0:
                return self.incorrect_user()
            confirmator.update_data(edt.text())
            if not cli_id:
                cli_id = confirmator.get_id()
            elif confirmator.get_id() != cli_id or not cli_id:
                return self.incorrect_user()
        text = self.pnt_edt.text().strip()
        if not len(text):
            return self.incorrect_pnt()

        self.__visit_id = self.save_graph(cli_id, text)

    @pyqtSlot()
    def on_close_btn_pressed(self):
        self.save_extra_info()
