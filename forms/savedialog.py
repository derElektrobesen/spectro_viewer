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
        self.connect_slots()

    def connect_slots(self):
        QObject.connect(self.measures_box, SIGNAL("currentIndexChanged(int)"), self.on_index_changed)
        QObject.connect(self.remove_measure_btn, SIGNAL("clicked()"), self.on_remove_graph_btn_clicked)
        QObject.connect(self.average_btn, SIGNAL("clicked()"), self.on_average_btn_clicked)

    def set_collection(self, collection):
        self.__collection = collection

    def set_measure_box_value(self):
        self.measures_box.clear()

        if not self.__collection:
            return

        m_format_str = translate("Measure", "Измерение") + ": %d"
        format_str = m_format_str + ", " + \
                translate("Spectr", "Спектр") + ": %d"
        for i, measure in enumerate(self.__collection):
            if measure.count() == 1:
                self.measures_box.addItem(m_format_str % (i + 1), { 'measure': i, 'graph': 0 })
            else:
                for j in range(measure.count()):
                    self.measures_box.addItem(format_str % (i + 1, j + 1), { 'measure': i, 'graph': j })

        self.on_index_changed(0)

    @pyqtSlot()
    def on_remove_graph_btn_clicked(self):
        i = self.measures_box.currentIndex()
        index = self.measures_box.itemData(i)
        self.__collection.get_measure(index['measure']).remove_graph_deffered(index['graph'])
        self.measures_box.removeItem(i)

    @pyqtSlot()
    def on_average_btn_clicked(self):
        index = self.measures_box.itemData(self.measures_box.currentIndex())
        measure = self.__collection.get_measure(index['measure'])
        measure.remove_deffered_graphs().average_graphs()
        self.__collection.set_measure(index['measure'], measure)
        self.set_measure_box_value()

    @pyqtSlot(int)
    def on_index_changed(self, index):
        index = self.measures_box.itemData(index)
        gr = self.__collection.get_measure(index['measure']).get_graph(index['graph'])
        self.cur_measure_wgt.set_graph("{measure}-{graph}".format(**index), gr)
        self.cur_measure_wgt.render()
