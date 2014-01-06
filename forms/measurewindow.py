from PyQt4.QtGui import *
from .measure_widget import Ui_measure_widget as UI_MeasureForm
from device import DeviceInspector

class MeasureWindow(QWidget, UI_MeasureForm):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.__inspector = DeviceInspector()
        self.__inspector.set_slots(data_came_slot = self.on_data_came,
                status_came_slot = self.on_status_came)

    def on_data_came(self):
        pass

    def on_status_came(self):
        pass

