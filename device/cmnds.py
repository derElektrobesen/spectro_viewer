from .modes import Modes, States

class Commands:
    @staticmethod
    def set_work_mode_cmd(mode):
        return b'c' + (b'1' if mode == Modes.continues else b'0') + b'>'

    @staticmethod
    def set_exp_time_cmd(time):
        return b'#exp=' + bytes(str(time), 'utf-8') + b'>'

    @staticmethod
    def start_metering_cmd(): return b's>'

    @staticmethod
    def stop_metering(): return b'p>'

    @staticmethod
    def interpret_device_state(cmd):
        pass

    @staticmethod
    def data_ends_flag(): return 62     # >

    @staticmethod
    def data_start_flag(): return 60    # <
    
    @staticmethod
    def status_start_flag(): return 58  # :
