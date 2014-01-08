from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import QSqlQuery
from db import DB
from .client_widget import Ui_patient_widget as UI_PatientForm

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

        q.prepare("select date, point, device, gr_id from diagrams_list where id = ?")
        q.bindValue(0, self.__pid)
        q.exec_()
        points = []
        i = 0
        while q.next():
            points.append({
                'date': q.value(0),
                'point': q.value(1),
                'device': q.value(2),
                'graph_id': q.value(3),
            })
            self.add_point(i, q.value(0) + " | " + q.value(1))
            i += 1
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

    def add_point(self, index, text):
        chb = QCheckBox(text)
        QObject.connect(chb, SIGNAL("stateChanged(int)"), self.on_point_checked)
        self.points_sca.widget().layout().addWidget(chb)

    @pyqtSlot(int)
    def on_point_checked(self, state):
        pass
