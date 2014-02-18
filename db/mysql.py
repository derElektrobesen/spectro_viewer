from PyQt4.QtSql import *
from PyQt4.QtCore import *
from PyQt4.QtSql import QSqlQuery

class SqlException(Exception):
    __msg = None
    def __init__(self, message = None, errcode = -1):
        if message:
            self.__msg = message
        if errcode:
            self.__errcode = errcode

    def errcode(self):
        return self.__errcode

    def __str__(self):
        return self.__msg or ""

class DB:
    @staticmethod
    def name():
        return 'spectroviewer_db'

    @staticmethod
    def con():
        return QSqlDatabase.database(DB.name())

    @staticmethod
    def query():
        return QSqlQuery(DB.con())

    @staticmethod
    def _import(fname):
        pass

    # Errors:
    #   -1: No names found
    @staticmethod
    def export(fname, without_names = []):
        to_export = {}
        names = []
        without_names = ', '.join(map(lambda e: str(e), without_names)) if len(without_names) else '-1'

        q = DB.query()
        q.prepare("select id, lastname, name, middlename, date_format(date, '%%d.%%m.%%Y') from Names where id not in (%s)" % without_names)
        q.exec_()

        while q.next():
            names.append(str(q.value(0)))
            to_export[q.value(0)] = {
                    'lastname': q.value(1),
                    'name': q.value(2),
                    'middlename': q.value(3),
                    'date': q.value(4),
            }
        q.finish()

        if not len(names):
            raise SqlException(errcode = 1)
        names = ', '.join(names)

        funcs = """
            export_main_info
            export_roles
            export_cards
        """

        for func in funcs.split():
            exec('to_export = DB.%s(to_export, names)' % func)

        print(to_export)

    @staticmethod
    def export_cards(to_export, ids):
        q = DB.query()
        q.prepare("select name_id, card_no from Cards where name_id in (%s)" % ids)
        q.exec_()
        while q.next():
            to_export[q.value(0)]['card_no'] = q.value(1)
        q.finish()
        return to_export

    @staticmethod
    def export_roles(to_export, ids):
        q = DB.query()
        q.prepare("select name_id, role from Roles where name_id in (%s)" % ids)
        q.exec_()

        while q.next():
            to_export[q.value(0)]['role'] = q.value(1)
        q.finish()

        return to_export

    @staticmethod
    def export_main_info(to_export, ids):
        q = DB.query()
        q.prepare("select name_id, eco_count, diagnosis, previous_treatment from MainInfo where name_id in (%s)" % ids)
        q.exec_()

        while q.next():
            ref = to_export[q.value(0)]
            ref['eco_count'] = q.value(1)
            ref['diagnosis'] = q.value(2)
            ref['treatment'] = q.value(3)
        q.finish()

        return to_export

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
