from PyQt4.QtSql import QSqlDatabase
from PyQt4.QtCore import QObject
from .db import SqlException, DB

class MySQL(QObject):
    def __init__(self, user, passw, action):
        self.__db = QSqlDatabase.addDatabase('QMYSQL', DB.name())
        self.__db.setHostName('localhost')
        self.__db.setDatabaseName('spectro_viewer')
        self.__db.setUserName(user)
        self.__db.setPassword(passw)

        if not self.__db.open():
            raise SqlException("Database open failure: %s" % self.__db.lastError().text())

        action.trigger()

    def close_connection(self):
        self.__db.close()
        self.__db = None
        QSqlDatabase.removeDatabase(DB.name())
