from PyQt4.QtGui import *
from PyQt4.QtCore import *
from .main_form import Ui_MainWindow as UI_MainWindow
from .addpatientwindow import AddPatientWindow
from .patientwindow import PatientWindow

class MainWindow(QMainWindow, UI_MainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.clients_w.clients_table.show_patient_signal.connect(self.add_patient_tab)
        self.__tabs = {}

    @pyqtSlot()
    def load_database(self):
        self.clients_w.load_database()

    @pyqtSlot()
    def on_act_add_client_triggered(self):
        callback = lambda: self.clients_w.update_database()
        wnd = AddPatientWindow(self, callback)
        wnd.show()

    @pyqtSlot(int)
    def add_patient_tab(self, pid):
        wnd = PatientWindow(self, pid)
        self.tabWidget.addTab(wnd, wnd.get_title())
