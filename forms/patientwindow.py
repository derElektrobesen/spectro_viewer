from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import QSqlQuery
from db import DB
from .client_widget import Ui_patient_widget as UI_PatientForm
from widgets import ColorWidget
from pr_core import translate, Graph
from settings import Settings

class PatientWindow(QWidget, UI_PatientForm):
    def __init__(self, parent = None, pid = None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.__pid = pid
        self.__info = {}
        self.__graphs = []
        self.__intacts = {}
        self.__info_widgets = {}
        self.__used_colors = {}

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

        q.prepare("select date, point, device, gr_id, point_type, intact_id from diagrams_list where id = ?")
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
                'intact_id': q.value(5),
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

    def get_color(self, key):
        color = None
        if key not in self.__used_colors.values():
            for c in Settings.colors:
                if c not in self.__used_colors:
                    self.__used_colors[c] = key
                    color = c
                    break
        else:
            for c in Settings.colors:
                if c in self.__used_colors and self.__used_colors[c] == key:
                    color = c
        return color or "#00ff00"

    def add_info_widgets(self, gid, name, key):
        if gid in self.__info_widgets:
            for w in self.__info_widgets[gid]:
                w.show()
            return
        
        def f(color):
            for w in self.__widgets:
                w.set_color(key, color)
            self.__used_colors[self.get_color(key)] = color

        l = self.colors_layout
        w = ColorWidget(color = self.get_color(key))
        w.on_color_change(f)
        self.__info_widgets[gid] = []
        self.__info_widgets[gid].append(w)
        row = l.rowCount()
        l.addWidget(w, row, 0)

        w = QLabel(name)
        self.__info_widgets[gid].append(w)
        l.addWidget(w, row, 1)

        w = QLabel("%.3f" % self.original_blue_sp_w.get_ia()[key])
        self.__info_widgets[gid].append(w)
        l.addWidget(w, row, 2)

        w = QLabel("%.3e" % self.original_blue_sp_w.get_s()[key])
        self.__info_widgets[gid].append(w)
        l.addWidget(w, row, 3)

    @pyqtSlot(int)
    def on_point_checked(self, state):
        chb = self.sender()
        key = None
        i_id = None
        gid = None
        name = None
        for point in self.__info['points']:
            if point['checkbox'] == chb:
                key = point['key']
                gid = point['graph_id']
                i_id = point['intact_id']
                name = point['point']
                break
        gr = None
        if i_id not in self.__intacts:
            self.__intacts[i_id] = Graph()
            self.__intacts[i_id].read_from_db(i_id)
        if state:
            gr = Graph()
            gr.read_from_db(gid)
            #gr = gr.smooth()

        for w in self.__widgets:
            if state:
                w.add_graph(key, gr, self.__intacts[i_id], color = self.get_color(key))
            else:
                w.remove_graph(key)
            w.render()

        if state:
            self.add_info_widgets(gid, name, key)
        else:
            for i in range(4):
                self.__info_widgets[gid][i].hide()
