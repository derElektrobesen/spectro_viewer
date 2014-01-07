from PyQt4.QtGui import *
from PyQt4.QtCore import *
from .measure_widget import Ui_measure_widget as UI_MeasureForm
from device import DeviceInspector
from pr_core import translate
from device import Modes, States

class MeasureWindow(QWidget, UI_MeasureForm):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.__inspector = DeviceInspector()
        self.__can_start = False
        self.__inspector.set_slots(data_came_slot = self.__on_data_came,
                status_came_slot = self.__on_status_came)
        QObject.connect(self.start_measure_btn, SIGNAL("clicked()"), self.__start_btn_pressed)
        QObject.connect(self.continiously_chb, SIGNAL("stateChanged(int)"), self.__mode_changed)
        QObject.connect(self.exposition_time_spb, SIGNAL("valueChanged(int)"), self.__exp_time_changed)

    def __on_data_came(self, graph):
        self.measure_viewer.set_graph(0, graph)
        self.measure_viewer.render()

    def __on_status_came(self, status):
        print(repr(status))
        self.__set_start_btn_state(status.state)
        self.__set_measure_mode(status.mode)
        self.__set_exp_time(status.exp_time)

    def __set_start_btn_state(self, state):
        enabled = True
        self.__can_start = False
        if state in [States.stopped, States.inactive, States.starting]:
            self.start_measure_btn.setText(translate("start_measure_btn", "Старт"))
            if state != States.stopped:
                enabled = False
            else:
                self.__can_start = True
        else:
            self.start_measure_btn.setText(translate("start_measure_btn", "Стоп"))
            if state != States.metering:
                enabled = False
        self.start_measure_btn.setEnabled(enabled)

    def __set_measure_mode(self, mode):
        self.continiously_chb.setChecked(mode == Modes.continues)

    def __set_exp_time(self, time):
        self.exposition_time_spb.setValue(int(time))

    @pyqtSlot()
    def __exp_time_changed(self, val):
        self.__inspector.set_exp_time(val)

    @pyqtSlot()
    def __start_btn_pressed(self):
        if self.__can_start:
            self.__inspector.start_metering()
        else:
            self.__inspector.stop_metering()

    @pyqtSlot(int)
    def __mode_changed(self, checked):
        self.__inspector.set_work_mode(Modes.continues if checked else Modes.single)
