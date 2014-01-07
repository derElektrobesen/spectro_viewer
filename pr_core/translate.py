from PyQt4.QtGui import QApplication

try:
    _encoding = QApplication.UnicodeUTF8
    def _tr(context, text, disambig = None):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _tr(context, text, disambig = None):
        return QApplication.translate(context, text, disambig)

translate = _tr
