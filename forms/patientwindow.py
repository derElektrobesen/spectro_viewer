from PyQt4.QtGui import *
from .client_widget import Ui_patient_widget as UI_PatientForm

class PatientWindow(QWidget, UI_PatientForm):
    def __init__(self, parent = None, pid = None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
