from PyQt4.QtCore import QObject, pyqtSignal, pyqtSlot
from socket import *
from .modes import DeviceStatus, Modes, States

class DeviceInspector(QObject):
    __socket = socket()

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
        pass
