from PyQt4.QtGui import *
from PyQt4.QtCore import *
from .login_form import Ui_LoginForm

class LoginWindow(QMainWindow, Ui_LoginForm):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.setAttribute(Qt.WA_ShowModal, true)

    def sql_connection(self):
        return None
