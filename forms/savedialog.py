from .save_dialog import Ui_MainWindow as Ui_SaveDialog
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import QObject, pyqtSlot, SIGNAL
from pr_core import translate

class SaveDialog(QMainWindow, Ui_SaveDialog):
    def __init__(self, parent = None, collection = None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.__collection = collection
        self.set_measure_box_value()
        QObject.connect(self.measures_box, SIGNAL("currentIndexChanged(int)"), self.on_index_changed)

    def set_collection(self, collection):
        self.__collection = collection

    def set_measure_box_value(self):
        if not self.__collection:
            self.measures_box.clear()
            return
        format_str = translate("Measure", "Измерение") + ": %d, " + \
                translate("Spectr", "Спектр") + ": %d"
        for i, measure in enumerate(self.__collection):
            for j in range(measure.count()):
                self.measures_box.addItem(format_str % (i + 1, j + 1), { 'measure': i, 'graph': j })

    @pyqtSlot(int)
    def on_index_changed(self, index):
        index = self.measures_box.itemData(index)
