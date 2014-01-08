from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSlot

from .extra_info_window import Ui_MainWindow

class ExtraInfoWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None, visit_id = 0):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.__visit_id = visit_id
