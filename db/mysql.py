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

        to_export = DB.__export_main_info(to_export, names)
        to_export = DB.__export_cards(to_export, names)
        to_export = DB.__export_roles(to_export, names)
        diagrams = DB.__export_visits(to_export, names)

        print(to_export)

    @staticmethod
    def __export_visits(to_export, ids):
        diagrams = []
        q = DB.query()
        q.prepare("""
            select v.name_id,
                   v.id,
                   date_format(v.date, '%%d.%%m.%%Y'),
                   t.treatment,
                   t.cycle_day,
                   t.endometrium,
                   t.scar,
                   t.fibrosis,
                   t.oncology,
                   t.other_info,
                   d.device,
                   d.point_name,
                   d.point_type,
                   d.id,
                   m.morfo,
                   m.meta,
                   m.funct
            from Visits v
            left join Treatment t on t.visit_id = v.id
            left join Diagrams d on d.visit_id = v.id
            left join Marks m on m.diagram_id = d.id
            where v.name_id in (%s)
        """ % ids)

        nu = lambda q, i: '' if type(q.value(i)) is QPyNullVariant else q.value(i)

        q.exec_()
        while q.next():
            ref = to_export[q.value(0)]
            if 'visits' not in ref:
                ref['visits'] = {}
            if q.value(1) not in ref['visits']:
                ref['visits'][q.value(1)] = {
                    'date':         nu(q, 2),
                    'treatment':    nu(q, 3),
                    'cycle_day':    nu(q, 4),
                    'endometrium':  nu(q, 5),
                    'scar':         nu(q, 6),
                    'fibrosis':     nu(q, 7),
                    'oncology':     nu(q, 8),
                    'other_info':   nu(q, 9),
                    'diagrams':     [],
                }
            ref['visits'][q.value(1)]['diagrams'].append({
                    'device':       nu(q, 10),
                    'point_name':   nu(q, 11),
                    'point_type':   nu(q, 12),
                    'id':           nu(q, 13),
                    'morfo':        nu(q, 14),
                    'meta':         nu(q, 15),
                    'funct':        nu(q, 16),
            })
            diagrams.append(q.value(13))
        q.finish()

        return ', '.join(map(lambda e: str(e), diagrams))

    @staticmethod
    def __export_cards(to_export, ids):
        q = DB.query()
        q.prepare("select name_id, card_no from Cards where name_id in (%s)" % ids)
        q.exec_()
        while q.next():
            to_export[q.value(0)]['card_no'] = q.value(1)
        q.finish()
        return to_export

    @staticmethod
    def __export_roles(to_export, ids):
        q = DB.query()
        q.prepare("select name_id, role from Roles where name_id in (%s)" % ids)
        q.exec_()

        while q.next():
            to_export[q.value(0)]['role'] = q.value(1)
        q.finish()

        return to_export

    @staticmethod
    def __export_main_info(to_export, ids):
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
