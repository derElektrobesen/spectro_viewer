from .save_dialog import Ui_MainWindow as Ui_SaveDialog
from PyQt4.QtGui import QMainWindow

class SaveDialog(QMainWindow, Ui_SaveDialog):
    def __init__(self, parent = None, collection = None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.__collection = collection

    def set_collection(self, collection):
        self.__collection = collection
