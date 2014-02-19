from PyQt4.QtSql import QSqlQuery, QSqlDatabase
from PyQt4.QtCore import QPyNullVariant
from .crypto import AESCipher
import pickle


class SqlException(Exception):
    __msg = None

    ErrcodeNoData           = 1
    ErrcodeNoFile           = 2
    ErrcodeDecryptFail      = 3
    ErrcodeIncorrectFormat  = 4

    ErrcodeDuplicateName    = 5

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
    __USE_B64_ENCRYPTION = False

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
    def import_db(fname, passw, get_answ_callback):
        f = None
        try:
            f = open(fname, "rb")
        except FileNotFoundError:
            raise SqlException(errcode = SqlException.ErrcodeNoFile)

        c = AESCipher(passw)
        data = f.read()
        if not len(data):
            raise SqlException(errcode = ErrcodeNoData)

        try:
            data = c.decrypt(data)
        except:
            raise SqlException(errcode = SqlException.ErrcodeDecryptFail)

        try:
            data = pickle.loads(data)
        except:
            raise SqlException(errcode = SqlException.ErrcodeIncorrectFormat)

        db = DB.con()
        db.transaction()
        try:
            DB.__import_data(data, get_answ_callback)
        except:
            db.rollback()
            raise
        else:
            db.commit()

    @staticmethod
    def __import_data(data, get_answ_callback):
        print(data['info'])
        return
        names = DB.__get_names()
        cur_visits = DB.__select_visits()
        graphs = []
        for card_no, patient in data['info'].items():
            if card_no in names:
                DB.__check_patient(names[card_no], patient, get_answ_callback)
            else:
                DB.__add_patient(names, patient, card_no)

            graphs.extend(DB.__parse_visits(names[patient['card_no']], patient['visits'], cur_visits))
        DB.__store_graphs(graphs, data['diagrams'])

    @staticmethod
    def __store_graphs(graphs, data):
        q = DB.query()
        q.prepare("insert into Data(diagram_id, point) values (?, POINT(?, ?))")
        for gr in graphs:
            q.bindValue(0, gr['diagram_id'])
            d = data[gr['id']]
            for p in d:
                q.bindValue(1, p[0])
                q.bindValue(2, p[1])
                q.exec_()

    @staticmethod
    def __parse_visits(name, visits, cur_visits):
        graphs = []
        for date, visit in visits.items():
            if name['id'] not in cur_visits or date not in cur_visits[name['id']]:
                visit_id = DB.__add_visit(name, visit, date)
                graphs.extend(DB.__parse_graphs_info(visit, date, visit_id))
                if name['id'] not in cur_visits:
                    cur_visits[name['id']] = []
                cur_visits[name['id']].append(date)

        return graphs

    @staticmethod
    def __parse_graphs_info(visit, date, visit_id):
        q = DB.query()
        q.prepare("insert into Diagrams(visit_id, device, point_name, point_type) values (?, ?, ?, ?)")
        r = []
        for gr in visit['diagrams']:
            q.bindValue(0, visit_id)
            q.bindValue(1, gr['device'])
            q.bindValue(2, gr['point_name'])
            q.bindValue(3, gr['point_type'])
            q.exec_()
            i = DB.__get_last_id()
            r.append({ 'diagram_id': i, 'id': gr['id'], })
        return r

    @staticmethod
    def __select_visits():
        q = DB.query()
        q.prepare("select id, date_format(date, '%d.%m.%Y') from Visits")
        q.exec_()
        r = {}
        while q.next():
            if q.value(0) not in r:
                r[q.value(0)] = []
            r[q.value(0)].append(q.value(1))
        return r

    @staticmethod
    def __get_last_id():
        q = DB.query()
        q.prepare("select last_insert_id()")
        q.exec_()
        q.next()
        r = q.value(0)
        q.finish()
        return r

    @staticmethod
    def __add_visit(name, visit, date):
        q = DB.query()
        q.prepare("insert into Visits(name_id, date) values (?, str_to_date(?, '%d.%m.%Y'))")
        q.bindValue(0, name['id'])
        q.bindValue(1, date)
        q.exec_()

        visit_id = DB.__get_last_id()
        q.prepare("insert into Treatment(visit_id, treatment, cycle_day, endometrium, scar, fibrosis, oncology, other_info) \
                    values (?, ?, ?, ?, ?, ?, ?, ?)")
        q.bindValue(0, visit_id)
        q.bindValue(1, visit['treatment'])
        q.bindValue(2, visit['cycle_day'])
        q.bindValue(3, visit['endometrium'])
        q.bindValue(4, visit['scar'])
        q.bindValue(5, visit['fibrosis'])
        q.bindValue(6, visit['oncology'])
        q.bindValue(7, visit['other_info'])
        q.exec_()

        q.prepare("insert into Marks(visit_id, morfo, meta, funct) values (?, ?, ?, ?)")
        q.bindValue(0, visit_id)
        q.bindValue(1, visit['morfo'])
        q.bindValue(2, visit['meta'])
        q.bindValue(3, visit['funct'])
        q.exec_()

        return visit_id

    @staticmethod
    def __check_patient(name, patient, get_answ_callback):
        if name['name'] != patient['name'] or \
           name['lastname'] != patient['lastname'] or \
           name['middlename'] != patient['middlename']:
            new_name = get_answ_callback(err_code = SqlException.ErrcodeDuplicateName,
                    name_1 = name, name_2 = patient)
            DB.__update_patient(_id = name['id'], new_name = new_name)

    @staticmethod
    def __update_patient(_id, new_name):
        q = DB.query()
        q.prepare("update Names set lastname = ?, name = ?, middlename = ? where id = ?")
        q.bindValue(0, new_name['lastname'])
        q.bindValue(1, new_name['name'])
        q.bindValue(2, new_name['middlename'])
        q.bindValue(3, _id)
        q.exec_()

    @staticmethod
    def __add_patient(names, patient, card_no):
        q = DB.query()
        q.prepare("call add_patient(?, ?, ?, ?, ?, ?, ?, ?)")
        q.bindValue(0, patient['lastname'])
        q.bindValue(1, patient['name'])
        q.bindValue(2, patient['middlename'])
        q.bindValue(3, card_no)
        q.bindValue(4, patient['date'])
        q.bindValue(5, patient['eco_count'])
        q.bindValue(6, patient['diagnosis'])
        q.bindValue(7, patient['treatment'])
        q.exec_()
        q.prepare("select name_id from Cards where card_no = ?")
        q.bindValue(0, card_no)
        q.exec_()
        q.next()
        names[card_no] = {
            'lastname'  : patient['lastname'],
            'name'      : patient['name'],
            'middlename': patient['middlename'],
            'id'        : q.value(0),
        }
        q.finish()

    @staticmethod
    def __get_names():
        q = DB.query()
        q.prepare("select id, lastname, name, middlename, card_no from select_all_names")
        q.exec_()
        r = {}
        while q.next():
            r[q.value(4)] = {
                    'id': q.value(0),
                    'lastname': q.value(1),
                    'name': q.value(2),
                    'middlename': q.value(3),
            }
        return r

    @staticmethod
    def export_db(fname, passw, without_names = []):
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
        to_export = DB.__swap_keys(to_export)
        to_export = DB.__export_diagrams({ 'info': to_export, }, diagrams)

        DB.__save_data(fname, passw, to_export)

    @staticmethod
    def __swap_keys(to_export):
        ids = list(to_export.keys())
        for i in ids:
            to_export[to_export[i]['card_no']] = to_export[i]
            if 'visits' in to_export[i]:
                ref = to_export[i]['visits']
                keys = list(ref.keys())
                for j in keys:
                    ref[ref[j]['date']] = ref[j]
                    del ref[j]['date']
                    del ref[j]
            del to_export[i]['card_no']
            del to_export[i]
        return to_export

    @staticmethod
    def __save_data(fname, passw, to_export):
        data = pickle.dumps(to_export, pickle.HIGHEST_PROTOCOL)
        c = AESCipher(passw, b64encode = DB.__USE_B64_ENCRYPTION)
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
            left join Marks m on m.visit_id = v.id
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
                    'morfo':        nu(q, 14),
                    'meta':         nu(q, 15),
                    'funct':        nu(q, 16),
                    'diagrams':     [],
                }
            ref['visits'][q.value(1)]['diagrams'].append({
                    'device':       nu(q, 10),
                    'point_name':   nu(q, 11),
                    'point_type':   nu(q, 12),
                    'id':           nu(q, 13),
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
