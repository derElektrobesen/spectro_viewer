from PyQt4.QtGui import *
from .main_form import Ui_MainWindow as UI_MainWindow

class MainWindow(QMainWindow, UI_MainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
