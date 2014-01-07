from PyQt4.QtGui import *
from .measure_widget import Ui_measure_widget as UI_MeasureForm
from device import DeviceInspector

class MeasureWindow(QWidget, UI_MeasureForm):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.__inspector = DeviceInspector()
        self.__inspector.set_slots(data_came_slot = self.__on_data_came,
                status_came_slot = self.__on_status_came)

    def __on_data_came(self, graph):
        self.measure_viewer.set_graph(0, graph)
        self.measure_viewer.render()

    def __on_status_came(self, status):
        print(repr(status))

    def __set_start_btn_state(self, state):
        pass
