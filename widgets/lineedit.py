from PyQt4.QtGui import QLineEdit
from PyQt4.QtCore import Qt

class LineEdit(QLineEdit):
    def __init__(self, parent = None):
        QLineEdit.__init__(self, parent)
        self.__backspace_pressed = False

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Backspace:
            self.__backspace_pressed = True
        else:
            self.__backspace_pressed = False
        QLineEdit.keyPressEvent(self, e)

    def is_backspace_pressed(self):
        return self.__backspace_pressed


