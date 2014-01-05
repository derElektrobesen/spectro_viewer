from PyQt4.QtGui import *
from PyQt4.QtSql import QSqlQuery, QSqlDatabase
from db import DB

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
    def __init__(self):
        QStandardItemModel.__init__(self)
        self.__set_header()

    def load_names(self):
        self.__query = QSqlQuery(DB.con())
        self.__query.prepare("call filter_names(?)")
        self.update_pattern()

    def __set_header(self):
        for index, column in enumerate(self.__columns):
            self.setHorizontalHeaderItem(index, QStandardItem(column))

    def add_row(self, data):
        pass

    def update_pattern(self, new_pat = ''):
        if not self.__query:
            return

        self.__query.bindValue(0, new_pat)
        self.__query.exec_()
        while (self.__query.next()):
            print("Hello")
            print(self.__query.value(0))

        query = QSqlQuery(DB.con())
        query.prepare("call filter_names('')")
        query.exec_()
        while (query.next()):
            print("Mysql hello")

        query.finish()

        query = QSqlQuery(DB.con())
        query.prepare("select * from Names")
        query.exec_()
        while (query.next()):
            print("Mysql")
        query.finish()

        self.__query.finish()

class ClientsTable(QTableView):
    __model = ClientTableModel()
    def __init__(self, parent = None):
        QTableView.__init__(self, parent)
        self.setModel(self.__model)
        self.horizontalHeader().setResizeMode(QHeaderView.Stretch)

    def load_names(self):
        return self.__model.load_names()
