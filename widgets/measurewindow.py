from PyQt4.QtGui import *
from forms import UI_MeasureForm

class MeasureWindow(QWidget, UI_MeasureForm):
    def __init__(seld, parent = None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
