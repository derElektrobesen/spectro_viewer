from .save_dialog import Ui_MainWindow as Ui_SaveDialog
from PyQt4.QtGui import QMainWindow, QStandardItemModel
from PyQt4.QtCore import QObject, pyqtSlot, SIGNAL
from PyQt4.QtSql import QSqlQuery
from pr_core import translate
from db import DB
import re

class ReqType:
    select_cards = 0
    select_names = 1

class CompleterModel(QStandardItemModel):
    def __init__(self, parent = None):
        QObject.QAbstractItemModel.__init__(self, parent)
        self.__req = None
        self.__select = QSqlQuery(DB.con())
        self.__select.prepare("select id, lastname, name, middlename, card_no from filtered_names")
        self.__old_rows = {}
        self.__rows = {}
        self.setSortRole(0)

    def update_data(self, text):
        if self.__req:
            p = re.compile('\s+')
            p.sub(text, ' ')
            self.__req.bindValue(0, text)
            self.__req.exec_()
            self.__req.finish()

            q = self.__select
            q.exec_()
            while q.next():
                self.add_row({
                    'id': q.value(0),
                    'lastname': q.value(1),
                    'name': q.value(2),
                    'middlename': q.value(3),
                    'card': q.value(4),
                })
            q.finish()

            for key, value in self.__old_rows.items():
                if key not in self.__rows:
                    self.takeRow(value.index().row())

    def add_row(self, row):
        if data['id'] not in self.__old_rows:
            row = []
            items = ['lastname', 'name', 'middlename'] if self.__req_type == ReqType.select_names else []
            items += ['card']
            for key in items:
                row.append(QStandardItem(data[key]))
            self.appendRow(row)
            self.__rows[data['id']] = row[0]
        else:
            self.__rows[data['id']] = self.__old_rows[data['id']]
        self.sort(self.sortRole())

    def set_request(self, req_type):
        self.__req = QSqlQuery(DB.con())
        text = None
        if req_type == ReqType.select_cards:
            text = 'call search_card("?")'
        elif req_type == ReqType.select_names:
            text = 'call filter_names("?")'
        if text:
            self.__req.prepare(req)
            self.__req_type = req_type

class SaveDialog(QMainWindow, Ui_SaveDialog):
    def __init__(self, parent = None, collection = None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.__collection = collection
        self.set_measure_box_value()
        self.connect_slots()
        self.set_completers()

    def connect_slots(self):
        QObject.connect(self.measures_box, SIGNAL("currentIndexChanged(int)"), self.on_index_changed)
        QObject.connect(self.remove_measure_btn, SIGNAL("clicked()"), self.on_remove_graph_btn_clicked)
        QObject.connect(self.average_btn, SIGNAL("clicked()"), self.on_average_btn_clicked)

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
        m = CompleterModel()
        m.set_request(ReqType.select_names)
        self.name_edt.setCompleter(QCompleter(m))

        m = CompleterModel()
        m.set_request(ReqType.select_cards)
        self.card_no_edt.setCompleter(QCompleter(m))

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
