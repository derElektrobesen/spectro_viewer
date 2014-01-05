from PyQt4.QtSql import *

class SqlException(Exception):
    __msg = None
    def __init__(self, message = None):
        if message:
            self.__msg = message

    def __str__(self):
        return self.__msg or ""

class DB:
    @staticmethod
    def name():
        return 'spectroviewer_db'

    def con():
        return QSqlDatabase.database(DB.name())

class MySQL:
    def __init__(self, user, passw):
        self.__db = QSqlDatabase.addDatabase('QMYSQL', DB.name())
        self.__db.setHostName('localhost')
        self.__db.setDatabaseName('spectro_viewer')
        self.__db.setUserName(user)
        self.__db.setPassword(passw)

        if not self.__db.open():
            raise SqlException("Database open failure: %s" % self.__db.lastError())

    def close_connection(self):
        self.__db.close()
        self.__db.removeDatabase(DB.name())
