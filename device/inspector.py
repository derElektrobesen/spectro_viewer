from PyQt4.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt4.QtCore import QThread, QCoreApplication
from socket import *
from select import select
from settings import Settings
from pr_core import Graph
from .modes import DeviceStatus, Modes, States
from .cmnds import Commands

class InspectorThread(QThread):
    status_str_came = pyqtSignal()
    data_block_came = pyqtSignal()
    device_disconnected = pyqtSignal()

    def __init__(self, parent = None):
        QThread.__init__(self, parent)
        self.__can_work = True
        self.__sock = None
        self.__last_data_block = None
        self.__last_device_status = None

    def run(self):
        while self.__can_work:
            if not self.__sock:
                self.msleep(1000)
            else:
                ready_read, ready_write, in_err = \
                    select([self.__sock], [], [], 1000)
                if self.__sock in ready_read:
                    self.ready_read(self.__sock)
            QCoreApplication.processEvents()

    def stop(self):
        self.__can_work = False

    def set_sock(self, sock):
        self.__sock = sock

    def ready_read(self, sock):
        block = b''
        while True:
            data = sock.recv(8192)
            if not len(data):
                self.stop()
                self.device_disconnected.emit()
                return
            block += data
            if block[-1] == Commands.data_ends_flag():
                break

        fl = block[0]
        block = block[1:-1]
        if fl == Commands.data_start_flag():
            self.on_data_block_came(block)
        elif fl == Commands.status_start_flag():
            self.on_status_block_came(block)

    def on_data_block_came(self, block):
        self.__last_data_block = Graph(dev_data = block)
        self.data_block_came.emit()

    def on_status_block_came(self, block):
        self.__last_device_status = Commands.decode_status(block)
        self.status_str_came.emit()

    def get_last_block(self):
        return self.__last_data_block.copy()

    def get_last_status(self):
        return self.__last_device_status.copy()

class DeviceInspector(QObject):
    __socket = socket()
    __inspector_thread = InspectorThread()

    device_starting     = pyqtSignal()
    device_stopped      = pyqtSignal()
    device_stopping     = pyqtSignal()
    device_connecting   = pyqtSignal()
    device_metering     = pyqtSignal()
    device_inactive     = pyqtSignal()

    data_coming = pyqtSignal()

    def __init__(self):
        super()
        self.__inspector_thread.data_block_came.connect(self.on_data_came)
        self.__inspector_thread.status_str_came.connect(self.on_status_came)
        self.__data_came_slot = self.__status_came_slot = None
        self.__connected = False
        self.connect()

    def connect(self):
        try:
            self.__socket.connect(('127.0.0.1', Settings.device_port))
            self.__inspector_thread.set_sock(self.__socket)
            self.__inspector_thread.start()
            self.__connected = True
        except ConnectionRefusedError as e:
            print("Can't to connect to device")

    def __send_cmd(self, cmd):
        if self.__connected:
            self.__socket.send(cmd)

    def set_exp_time(self, time):
        self.__send_cmd(Commands.set_exp_time_cmd(time))

    def set_work_mode(self, mode):
        self.__send_cmd(Commands.set_work_mode_cmd(mode))

    def start_metering(self):
        self.__send_cmd(Commands.start_metering_cmd())

    def stop_metering(self):
        self.__send_cmd(Commands.stop_metering_cmd())

    def set_slots(self, data_came_slot = None, status_came_slot = None):
        self.__data_came_slot = data_came_slot
        self.__status_came_slot = status_came_slot

    @pyqtSlot()
    def on_data_came(self):
        return self.__data_came_slot and self.__data_came_slot(self.__inspector_thread.get_last_block())

    @pyqtSlot()
    def on_status_came(self):
        return self.__status_came_slot and self.__status_came_slot(self.__inspector_thread.get_last_status())

    def disconnect(self):
        if self.__inspector_thread:
            self.__inspector_thread.stop()
            self.__inspector_thread.wait()
