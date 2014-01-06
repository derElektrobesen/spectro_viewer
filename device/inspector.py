from PyQt4.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt4.QtCore import QThread, QCoreApplication
from socket import *
from .modes import DeviceStatus, Modes, States
from settings import Settings

class InspectorThread(QThread):
    def __init__(self, parent = None):
        QThread.__init__(self, parent)
        self.__can_work = True
        self.__sock = None

    def run():
        while self.__can_work:
            print("Hello")
            QCoreApplication.processEvents()
            self.msleep(1000)

    def stop():
        self.__can_work = False

    def set_socket(self, sock):
        self.__sock = sock

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
        self.__signals = {
            States.inactive:    self.device_inactive,
            States.starting:    self.device_starting,
            States.metering:    self.device_metering,
            States.stopping:    self.device_stopping,
            States.stopped:     self.device_stopped,
            States.connecting:  self.device_connecting,
        }

    def reconnect(self):
        self.__inspector_thread.stop()
        self.__inspector_thread.quit()
        self.__socket.close()
        self.__socket.connect(('127.0.0.1', Settings.device_port))
        self.__inspector_thread.set_sock(self.__socket)
        self.__inspector_thread.start()
