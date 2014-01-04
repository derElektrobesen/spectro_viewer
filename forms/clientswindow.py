from PyQt4.QtGui import *
from .clients_table_widget import Ui_clients_widget as UI_ClientForm

class ClientsWindow(QWidget, UI_ClientForm):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
