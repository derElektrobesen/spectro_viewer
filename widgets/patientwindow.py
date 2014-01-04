from PyQt4.QtGui import *
from forms import UI_PatientForm

class PatientWindow(QWidget, UI_PatientForm):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
