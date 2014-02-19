from PyQt4.QtSql import QSqlQuery, QSqlDatabase
from .crypto import AESCipher
import pickle


class SqlException(Exception):
    __msg = None

    ErrcodeNoData = 1

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
    def export(fname, passw, without_names = []):
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
            raise SqlException(errcode = SqlException.ErrcodeNoData)
        names = ', '.join(names)

        to_export = DB.__export_main_info(to_export, names)
        to_export = DB.__export_cards(to_export, names)
        to_export = DB.__export_roles(to_export, names)
        diagrams  = DB.__export_visits(to_export, names)
        to_export = { 'info': to_export, }
        to_export = DB.__export_diagrams(to_export, diagrams)

        DB.__save_data(fname, passw, to_export)

    @staticmethod
    def __save_data(fname, passw, to_export):
        data = pickle.dumps(to_export, pickle.HIGHEST_PROTOCOL)
        c = AESCipher(passw, b64encode = False)
        open(fname, 'wb').write(c.encrypt(data))

    @staticmethod
    def __export_diagrams(to_export, ids):
        q = DB.query()
        q.prepare("select diagram_id, x(point), y(point) from Data where diagram_id in (%s) order by id" % ids)
        q.exec_()

        d = to_export['diagrams'] = {}

        while q.next():
            if q.value(0) not in d:
                d[q.value(0)] = []
            d[q.value(0)].append((q.value(1), q.value(2)))

        q.finish()
        return to_export

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
