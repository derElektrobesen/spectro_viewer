from PyQt4.QtCore import QObject, pyqtSlot, pyqtSignal

def _composed(*decs):
    def deco(f):
        for dec in reversed(decs):
            f = dec(f)
        return f
    return deco

_st_prop = _composed(staticmethod, property)

class Modes:
    @_st_prop
    def single(): return 0

    @_st_prop
    def continues(): return 1

class States:
    @_st_prop
    def inactive(): return 0

    @_st_prop
    def starting(): return 1

    @_st_prop
    def metering(): return 2

    @_st_prop
    def stopping(): return 3

    @_st_prop
    def stopped(): return 4
    
    @_st_prop
    def connecting(): return 5

class DeviceMode(QObject):
    mode_changed = pyqtSignal()

    def __init__(self, mode = Modes.continues):
        super()
        self.__mode = mode

    @property
    def single(self):
        return self.__mode == Modes.single

    @property
    def continues(self):
        return self.__mode == Modes.continues

    @pyqtSlot()
    def change_mode(self, new_mode):
        if self.__mode != new_mode:
            self.__mode = new_mode
            self.mode_changed.emit()

class DeviceState(QObject):
    __state = States.stopped

    @property
    def state(self): return self.__state

    @state.setter
    def state(self, val): self.__state = val

class DeviceStatus(QObject):
    __mode = DeviceMode()
    __state = DeviceState()
    
    @property
    def mode_changed(self):
        return self.__mode.mode_changed

    @property
    def state(self):
        return self.__state.state

    @state.setter
    def state(self, new_state):
        self.__state.state = new_state
