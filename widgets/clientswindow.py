from PyQt4.QtGui import *
from forms import UI_ClientForm

class ClientsWindow(QWidget, UI_ClientForm):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
