from PyQt4.QtGui import *
from PyQt4.QtCore import pyqtSlot, pyqtSignal, QObject, SIGNAL
from PyQt4.QtSql import QSqlQuery, QSqlDatabase, QSql
from db import DB
from pr_core import translate
import os
import re

# TODO
class ButtonDelegate(QStyledItemDelegate):
    def createButton(parent, option, index):
        btn = QPushButton(parent)
        return btn

    def updateGeometry(widget, option, index):
        widget.setGeometry(option.rect)

class ClientTableModel(QStandardItemModel):
    __columns = [translate('clienttablemodel', 'Фамилия'), translate('clienttablemodel', 'Имя'),
                 translate('clienttablemodel', 'Отчество'), translate('clienttablemodel', 'Номер карты')]
    __query = None
    __pid = os.getpid()
    __rows = {}

    def __init__(self):
        QStandardItemModel.__init__(self)
        self.__set_header()
        self.setSortRole(0)

    def load_names(self):
        self.__query = QSqlQuery(DB.con())
        self.__query.prepare("call filter_names(?)")
        self.__data_q = QSqlQuery(DB.con())
        self.__data_q.prepare("select id, lastname, name, middlename, card_no from filtered_names")
        self.update_pattern()

    def __set_header(self):
        for index, column in enumerate(self.__columns):
            self.setHorizontalHeaderItem(index, QStandardItem(column))

    def __add_row(self, data):
        if data['id'] not in self.__old_rows:
            row = []
            for key in ['lastname', 'name', 'middlename', 'card']:
                row.append(QStandardItem(data[key]))
                row[-1].setEditable(False)
            self.appendRow(row)
            self.__rows[data['id']] = row[0]
        else:
            self.__rows[data['id']] = self.__old_rows[data['id']]
        self.sort(self.sortRole())

    def get_row_id(self, model_index):
        item = self.item(model_index.row())
        for key, row in self.__rows.items():
            if item == row:
                return key
        return None

    def update_pattern(self, new_pat = ''):
        if not self.__query:
            return

        self.__old_rows = self.__rows
        self.__rows = {}

        self.__query.bindValue(0, new_pat)
        self.__query.exec_()
        self.__query.finish()

        q = self.__data_q
        q.exec_()
        while q.next():
            self.__add_row({
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

class ClientsTable(QTableView):
    __model = ClientTableModel()
    show_patient_signal = pyqtSignal(int)

    def __init__(self, parent = None):
        QTableView.__init__(self, parent)
        self.setModel(self.__model)
        self.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        QObject.connect(self, SIGNAL("doubleClicked(QModelIndex)"), self.on_row_double_clicked)

    def load_names(self):
        return self.__model.load_names()

    @pyqtSlot()
    def update_list(self, pat):
        p = re.compile('\s+')
        p.sub(pat, ' ')
        return self.__model.update_pattern(pat)

    @pyqtSlot("QModelIndex")
    def on_row_double_clicked(self, index):
        data = self.__model.get_row_id(index)
        self.show_patient_signal.emit(data)
