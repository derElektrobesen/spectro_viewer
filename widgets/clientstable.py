from PyQt4.QtGui import *
from PyQt4.QtSql import QSqlQuery, QSqlDatabase, QSql
from db import DB
import os

try:
    _encoding = QApplication.UnicodeUTF8
    def _tr(context, text, disambig = None):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _tr(context, text, disambig = None):
        return QApplication.translate(context, text, disambig)

# TODO
class ButtonDelegate(QStyledItemDelegate):
    def createButton(parent, option, index):
        btn = QPushButton(parent)
        return btn

    def updateGeometry(widget, option, index):
        widget.setGeometry(option.rect)

class ClientTableModel(QStandardItemModel):
    __columns = [_tr('clienttablemodel', 'Фамилия'), _tr('clienttablemodel', 'Имя'),
                 _tr('clienttablemodel', 'Отчество'), _tr('clienttablemodel', 'Номер карты')]
    __query = None
    __pid = os.getpid()
    def __init__(self):
        QStandardItemModel.__init__(self)
        self.__set_header()

    def load_names(self):
        self.__query = QSqlQuery(DB.con())
        self.__query.prepare("call filter_names(?)")
        self.__data_q = QSqlQuery(DB.con())
        self.__data_q.prepare("select id, lastname, name, middlename, card_no from filtered_names")
        self.update_pattern()

    def __set_header(self):
        for index, column in enumerate(self.__columns):
            self.setHorizontalHeaderItem(index, QStandardItem(column))

    def add_row(self, data):
        print(data)

    def update_pattern(self, new_pat = ''):
        if not self.__query:
            return

        self.__query.bindValue(0, new_pat)
        self.__query.exec_()
        self.__query.finish()

        q = self.__data_q
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

class ClientsTable(QTableView):
    __model = ClientTableModel()
    def __init__(self, parent = None):
        QTableView.__init__(self, parent)
        self.setModel(self.__model)
        self.horizontalHeader().setResizeMode(QHeaderView.Stretch)

    def load_names(self):
        return self.__model.load_names()
