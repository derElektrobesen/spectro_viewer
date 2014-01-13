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
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.tabBar().tabButton(0, QTabBar.RightSide).resize(0, 0);
        self.tabWidget.tabBar().tabButton(1, QTabBar.RightSide).resize(0, 0);

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
        if pid not in self.__tabs:
            wnd = PatientWindow(self, pid)
            self.__tabs[pid] = self.tabWidget.addTab(wnd, wnd.get_title())
        self.tabWidget.setCurrentIndex(self.__tabs[pid])

    @pyqtSlot(int)
    def on_tabWidget_tabCloseRequested(self, tab):
        k = None
        for key, val in self.__tabs.items():
            if val == tab:
                k = key
            elif val > tab:
                self.__tabs[key] -= 1
        if k:
            del self.__tabs[k]
        self.tabWidget.removeTab(tab)
