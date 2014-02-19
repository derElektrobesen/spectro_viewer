from PyQt4.QtCore import *
from PyQt4.QtGui import *
from .results import Ui_ResultsWindow

class ResultsDialog(QDialog, Ui_ResultsWindow):
    def __init__(self, parent = None, callback = None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.__data = None
        self.__callback = callback

    @pyqtSlot()
    def on_ok_btn_clicked(self):
        self.__data = {}
        for key in "morfo meta funct".split():
            if self.findChild(QRadioButton, key + '_p').isChecked():
                self.__data[key] = '+'
            elif self.findChild(QRadioButton, key + '_m').isChecked():
                self.__data[key] = '-'
            else:
                self.__data[key] = '+-'
        self.close()
        if self.__callback:
            self.__callback(self.__data)
