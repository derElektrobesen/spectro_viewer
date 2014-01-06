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

class DeviceStatus(QObject):
    def __init__(self, state = States.inactive, mode = Modes.single, frames_count = 0, exp_time = 0):
        self.__mode = mode
        self.__state = state
        self.__frames_count = frames_count
        self.__exp_time = exp_time

    def copy(self):
        return DeviceStatus(state = self.state, mode = self.mode,
                frames_count = self.frames_count, exp_time = self.exp_time)
    
    @property
    def state(self):
        return self.__state.state

    @state.setter
    def state(self, new_state):
        self.__state.state = new_state

    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, val):
        self.__mode = val

    @property
    def frames_count(self):
        return self.__frames_count

    @frames_count.setter
    def frames_count(self, val):
        self.__frames_count = float(val)

    @property
    def exp_time(self):
        return self.__exp_time

    @exp_time.setter
    def exp_time(self, val):
        self.__exp_time = val
