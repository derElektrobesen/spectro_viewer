from PyQt4.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt4.QtCore import QThread, QCoreApplication
from socket import *
from select import select
from settings import Settings
from .modes import DeviceStatus, Modes, States
from .cmnds import Commands

class InspectorThread(QThread):
    status_str_came = pyqtSignal()
    data_block_came = PyqtSignal()

    def __init__(self, parent = None):
        QThread.__init__(self, parent)
        self.__can_work = True
        self.__sock = None

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
            block += data
            if block[-1] == Commands.data_ends_flag():
                break

        block = block[1:-1]
        str_block = block.decode('utf-8')

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
        self.connect()

    def connect(self):
        self.__socket.connect(('127.0.0.1', Settings.device_port))
        self.__inspector_thread.set_sock(self.__socket)
        self.__inspector_thread.start()
