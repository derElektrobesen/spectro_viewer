from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import QSqlQuery
from db import DB
from .client_widget import Ui_patient_widget as UI_PatientForm
from pr_core import translate, Graph

class PatientWindow(QWidget, UI_PatientForm):
    def __init__(self, parent = None, pid = None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.__pid = pid
        self.__info = {}
        self.__graphs = []

        self.__widgets = (
            self.blue_sp_w, self.red_sp_w, self.original_blue_sp_w,
            self.original_red_sp_w, self.differentiated_blue_sp_w,
            self.differentiated_red_sp_w, self.intact_blue_sp_w,
            self.intact_red_sp_w)

        self.get_main_info()
        self.set_main_values()

    def get_main_info(self):
        q = QSqlQuery(DB.con())
        q.prepare("call select_main_info(?)")
        q.bindValue(0, self.__pid)
        q.exec_()
        q.finish()

        q.prepare("select `id`, `name`, `lastname`, `middlename`, \
                `age`, `eco_count`, `diagnosis`, `incomes` from `main_info_results`")
        q.exec_()
        q.next()
        self.__info = {
            'name': q.value(1),
            'lastname': q.value(2),
            'middlename': q.value(3),
            'age': q.value(4),
            'eco_count': q.value(5),
            'diagnosis': q.value(6),
            'incomes': q.value(7),
        }
        q.finish()

        if not self.__info['incomes']:
            self.__info['incomes'] = 0

        q.prepare("select date, point, device, gr_id, point_type from diagrams_list where id = ?")
        q.bindValue(0, self.__pid)
        q.exec_()
        points = []
        while q.next():
            points.append({
                'date': q.value(0),
                'point': q.value(1),
                'device': q.value(2),
                'graph_id': q.value(3),
                'type': q.value(4),
                'key': q.value(0) + q.value(1) + str(len(points)),
            })
            points[-1]['checkbox'] = self.add_point(q.value(0) + " | " + q.value(1) + \
                    (translate("intact", " (интакт)") if q.value(4) == 'intact' else ''))
        q.finish()

        w = QWidget()
        w.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.points_sca.widget().layout().addWidget(w)

        self.__info['points'] = tuple(points)

    def get_title(self):
        return self.__info['lastname'] + " " + self.__info['name'][0] + ". " + \
            self.__info['middlename'][0] + "."

    def set_main_values(self):
        ref = self.__info
        self.name_lbl.setText(ref['lastname'] + ' ' + ref['name'] + " " + ref['middlename'])
        self.age_lbl.setText(str(ref['age']))
        self.incomes_lbl.setText(str(ref['incomes']))
        self.diagnosis_lbl.setText(ref['diagnosis'])

    def add_point(self, text):
        chb = QCheckBox(text)
        QObject.connect(chb, SIGNAL("stateChanged(int)"), self.on_point_checked)
        self.points_sca.widget().layout().addWidget(chb)
        return chb

    @pyqtSlot(int)
    def on_point_checked(self, state):
        chb = self.sender()
        key = None
        vid = None
        for point in self.__info['points']:
            if point['checkbox'] == chb:
                key = point['key']
                vid = point['graph_id']
                break
        gr = None
        if state:
            gr = Graph()
            gr.read_from_db(vid)
            gr = gr.smooth()
        for w in self.__widgets:
            if state:
                w.add_graph(key, gr)
            else:
                w.remove_graph(key)
            w.render()
