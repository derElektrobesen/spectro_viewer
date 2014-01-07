from .save_dialog import Ui_MainWindow as Ui_SaveDialog
from PyQt4.QtGui import QMainWindow, QStandardItemModel, QStandardItem, QCompleter
from PyQt4.QtCore import QObject, pyqtSlot, SIGNAL, Qt
from PyQt4.QtSql import QSqlQuery
from pr_core import translate
from db import DB
import re

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
        elif req_type == ReqType.select_names:
            text = 'call search_name(?)'
        if text:
            self.__req.prepare(text)
            self.__req_type = req_type

    def get_text(self):
        return self.__data and self.__data['text']

    def get_data(self):
        return self.__data

DEBUG = True

class SaveDialog(QMainWindow, Ui_SaveDialog):
    def __init__(self, parent = None, collection = None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.__collection = collection
        self.__do_text_search = True

        global DEBUG
        if not DEBUG:
            self.set_measure_box_value()

        self.connect_slots()
        self.set_completers()

    def connect_slots(self):
        QObject.connect(self.measures_box, SIGNAL("currentIndexChanged(int)"), self.on_index_changed)
        QObject.connect(self.remove_measure_btn, SIGNAL("clicked()"), self.on_remove_graph_btn_clicked)
        QObject.connect(self.average_btn, SIGNAL("clicked()"), self.on_average_btn_clicked)
        QObject.connect(self.name_edt, SIGNAL("textChanged(QString)"), self.on_main_text_changed)
        QObject.connect(self.card_no_edt, SIGNAL("textChanged(QString)"), self.on_main_text_changed)

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

    def set_progress(self, val):
        self.progressBar.setValue(val)

    def set_completers(self):
        m = CompleterText()
        m.set_request(ReqType.select_names)
        self.name_edt_lines = m

        m = CompleterText()
        m.set_request(ReqType.select_cards)
        self.card_no_lines = m

    @pyqtSlot()
    def on_remove_graph_btn_clicked(self):
        self.set_progress(0)
        if self.measures_box.count() > 1:
            i = self.measures_box.currentIndex()
            index = self.measures_box.itemData(i)
            self.__collection.get_measure(index['measure']).remove_graph_deffered(index['graph'])
            self.measures_box.removeItem(i)
        if self.measures_box.count() == 1:
            self.remove_measure_btn.setEnabled(False)
        self.set_progress(100)

    @pyqtSlot()
    def on_average_btn_clicked(self):
        self.set_progress(0)
        index = self.measures_box.itemData(self.measures_box.currentIndex())
        if index:
            measure = self.__collection.get_measure(index['measure'])
            measure = measure.remove_deffered_graphs().average_graphs()
            self.__collection.set_measure(index['measure'], measure)
            self.set_measure_box_value()
        self.set_progress(100)

    @pyqtSlot(int)
    def on_index_changed(self, index):
        index = self.measures_box.itemData(index)
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
        if ref:
            ref.update_data(text)
            t = ref.get_text()
            if t:
                self.__do_text_search = False
                edt.setText(t)
                edt.setSelection(len(text), len(t) - len(text))
