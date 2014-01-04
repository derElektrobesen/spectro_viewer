from PyQt4.QtGui import *
from .measure_widget import Ui_measure_widget as UI_MeasureForm

class MeasureWindow(QWidget, UI_MeasureForm):
    def __init__(seld, parent = None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
