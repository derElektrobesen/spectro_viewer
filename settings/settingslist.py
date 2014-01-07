import os

class SettingsList:
    fname = os.path.dirname(os.path.abspath(__file__)) + '/settings.cfg'
    settings = {
        'device_port':  50009,        
        'device_type':  '"blue"',
    }
