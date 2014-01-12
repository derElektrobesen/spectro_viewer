from PyQt4.QtGui import *
from PyQt4.QtCore import *
from .measure_widget import Ui_measure_widget as UI_MeasureForm
from .savedialog import SaveDialog
from device import DeviceInspector
from pr_core import translate, MeasureCollection
from device import Modes, States

class MeasureWindow(QWidget, UI_MeasureForm):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.__inspector = DeviceInspector()
        self.__can_start = False
        self.__collection = MeasureCollection()
        self.__inspector.set_slots(data_came_slot = self.__on_data_came,
                status_came_slot = self.__on_status_came)
        self.bind_slots()

    def bind_slots(self):
        QObject.connect(self.start_measure_btn, SIGNAL("clicked()"), self.__start_btn_pressed)
        QObject.connect(self.clean_hist_btn, SIGNAL("clicked()"), self.__clean_collection)
        QObject.connect(self.process_measure_btn, SIGNAL("clicked()"), self.__show_collection)
        QObject.connect(self.continiously_chb, SIGNAL("stateChanged(int)"), self.__mode_changed)
        QObject.connect(self.exposition_time_spb, SIGNAL("valueChanged(int)"), self.__exp_time_changed)
        QObject.connect(self, SIGNAL("destroyed()"), self.on_close)
        QObject.connect(self.remove_voice_chb, SIGNAL("stateChanged(int)"), self.set_smooth_mode)

    def __on_data_came(self, graph):
        if not graph:
            return
        if self.remove_voice_chb.isChecked():
            graph = graph.smooth()
        self.measure_viewer.set_graph(0, graph)
        self.measure_viewer.render()
        self.__collection.add_graph(graph)

    def __on_status_came(self, status):
        print(repr(status))
        self.__set_start_btn_state(status.state)
        self.__set_measure_mode(status.mode)
        self.__set_exp_time(status.exp_time)

    def __set_start_btn_state(self, state):
        enabled = True
        self.__can_start = False
        if state in [States.stopped, States.inactive, States.starting]:
            self.start_measure_btn.setText(translate("start_measure_btn", "Старт"))
            if state != States.stopped:
                enabled = False
            else:
                self.__can_start = True
        else:
            self.start_measure_btn.setText(translate("start_measure_btn", "Стоп"))
            if state != States.metering:
                enabled = False
        self.start_measure_btn.setEnabled(enabled)
        enabled = self.__can_start and not self.__collection.empty()
        self.process_measure_btn.setEnabled(enabled)
        self.clean_hist_btn.setEnabled(enabled)

    def __set_measure_mode(self, mode):
        self.continiously_chb.setChecked(mode == Modes.continues)

    def __set_exp_time(self, time):
        self.exposition_time_spb.setValue(int(time))

    @pyqtSlot()
    def on_close(self):
        self.__inspector.disconnect()

    @pyqtSlot()
    def __clean_collection(self):
        res = QMessageBox.information(self, translate("clean_collection", "Очистить историю"),
                translate("clean_collection", "Вы уверены, что хотите удалить все " +
                          "считанные спектры?"),
                translate("yes", "Да"), translate("no", "Нет"))
        if res == 0:
            del self.__collection
            self.__collection = MeasureCollection()

    @pyqtSlot(int)
    def __exp_time_changed(self, val):
        self.__inspector.set_exp_time(val)

    @pyqtSlot()
    def __start_btn_pressed(self):
        if self.__can_start:
            self.__inspector.start_metering()
            self.__collection.init_collection()
        else:
            self.__inspector.stop_metering()

    @pyqtSlot(int)
    def __mode_changed(self, checked):
        self.__inspector.set_work_mode(Modes.continues if checked else Modes.single)

    @pyqtSlot()
    def __show_collection(self):
        d = SaveDialog(self, self.__collection)
        d.show()

    @pyqtSlot(int)
    def set_smooth_mode(self, enabled):
        self.__on_data_came(self.measure_viewer.get_graph(0))
