from PyQt4.QtCore import QObject, pyqtSlot, pyqtSignal
from PyQt4.QtGui import QApplication
from pr_core import translate

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
        QObject.__init__(self)
        self.__mode = mode
        self.__state = state
        self.__frames_count = frames_count
        self.__exp_time = exp_time

    def copy(self):
        return DeviceStatus(state = self.__state, mode = self.__mode,
                frames_count = self.__frames_count, exp_time = self.__exp_time)

    def __str__(self):
        return translate("DeviceStatus",
            "Статус: {state}; Режим: {mode};".format(
            state = {
                States.inactive:    translate("State", "Неактивен"),
                States.starting:    translate("State", "Старт"),
                States.metering:    translate("State", "Измерение"),
                States.stopping:    translate("State", "Остановка"),
                States.stopped:     translate("State", "Остановлен"),
                States.connecting:  translate("State", "Подключение"),
            }[self.__state], mode = {
                Modes.single:       translate("Modes", "Одиночный"),
                Modes.continues:    translate("Modes", "Непрерывный"),
            }[self.__mode]))

    def __repr__(self):
        return translate("DeviceStatus",
            "{start} Кадров/с: {frames}; Время эксп.: {exp}".format(
            frames = self.__frames_count, exp = self.__exp_time, start = self.__str__()))
    
    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, new_state):
        self.__state = new_state

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
