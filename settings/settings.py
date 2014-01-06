from pickle import dump, load
import os

class __Args:
    fname = os.path.dirname(os.path.abspath(__file__)) + '/settings.cfg'
    settings = {
        'device_port':  50009,        
    }

def __read_settings():
    ref = {}

    if os.path.isfile(__Args.fname):
        ref = load(open(__Args.fname, "rb"))
    __Args.settings.update(ref)

    code = ''

    for key, value in __Args.settings.items():
        code += """
    @staticmethod
    def __get_{name}(cls): return __Args.settings['{name}']

    @staticmethod
    def __set_{name}(cls, val): __Args.settings['{name}'] = val

    {name} = property(__get_{name}, __set_{name})
    {name} = {value}
        """.format(name = key, value = value)

    return code

__code = """
class Settings:
    @staticmethod
    def store():
        dump(__Args.settings, open(__Args.__fname, "wb"))

"""

exec(__code + __read_settings())
