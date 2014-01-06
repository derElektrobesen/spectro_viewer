from pickle import dump, load
import os

class Settings:
    __fname = os.path.dirname(os.path.abspath(__file__)) + '/settings.cfg'
    __settings = {
        'device_port':  50009,        
    }

    @staticmethod
    def read_settings(cls):
        ref = {}
        if os.path.isfile(cls.__fname):
            ref = load(open(cls.__fname, "rb"))
        cls.__settings.update(ref)

        code = ''

        for key, value in cls.__settings.items():
            code += """
    class class_{name}:
        @staticmethod
        def __get_{name}(cls): return cls.__settings['{name}']

        @staticmethod
        def __set_{name}(cls, val): cls.__settings['{name}'] = val

        {name} = property(__get_{name}, __set_{name})
        {name} = {value}
            """.format(name = key, value = value)
        exec(code)
        return code

    @staticmethod
    def store(cls):
        dump(cls.__settings, open(cls.__fname, "wb"))
