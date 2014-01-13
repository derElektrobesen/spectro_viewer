import os

class SettingsList:
    fname = os.path.dirname(os.path.abspath(__file__)) + '/settings.cfg'
    settings = {
        'device_port':  50009,        
        'device_type':  '"blue"',
        'colors': '"#ff0000 #00ff00 #0000ff #ffff00 #00ffff #ff00ff #c0c0c0 #600000
                    #009900 #339999 #cc6633 #ff3300".split()'
    }
