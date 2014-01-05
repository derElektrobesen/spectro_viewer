from PyQt4.QtGui import *
from PyQt4.QtCore import *
from .main_form import Ui_MainWindow as UI_MainWindow

class MainWindow(QMainWindow, UI_MainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

    @pyqtSlot()
    def load_database(self):
        self.clients_w.load_database()
