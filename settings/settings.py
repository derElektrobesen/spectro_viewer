from .settingslist import SettingsList
from pickle import dump, load
import os

def __read_settings():
    ref = {}

    if os.path.isfile(SettingsList.fname):
        ref = load(open(SettingsList.fname, "rb"))
    SettingsList.settings.update(ref)

    code = ''

    for key, value in SettingsList.settings.items():
        code += """

    @staticmethod
    def __get_{name}(cls): return SettingsList.settings['{name}']

    @staticmethod
    def __set_{name}(cls, val): SettingsList.settings['{name}'] = val

    {name} = property(__get_{name}, __set_{name})
    {name} = {value}

        """.format(name = key, value = value)

    return code

__code = """
class Settings:
    @staticmethod
    def store():
        dump(SettingsList.settings, open(SettingsList.fname, "wb")) # TODO

"""

exec(__code + __read_settings())
