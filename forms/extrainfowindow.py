from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtSql import QSqlQuery
from db import DB

from .extra_info_window import Ui_MainWindow

class ExtraInfoWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None, visit_id = 0):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.__visit_id = visit_id

    @pyqtSlot()
    def on_close_btn_pressed(self):
        f = lambda b: "TRUE" if b else "FALSE"
        data = {
            'cycle':    self.cycle.value(),
            'endo':     self.endometrium.text(),
            'scars':    f(self.scars.isChecked()),
            'fibrosis': f(self.fibrosis.isChecked()),
            'onco':     self.oncology.toPlainText(),
            'research': self.researches.toPlainText(),
            'treat':    self.treatment.toPlainText(),
            'visit':    self.__visit_id,
        }
        q = QSqlQuery(DB.con())
        q.prepare("insert into Treatment(visit_id, treatment, cycle_day, endometrium, " +
                "scar, fibrosis, oncology, other_info) values (:visit, :treat, :cycle, " +
                ":endo, :scars, :fibrosis, :onco, :research)")
        for key, val in data:
            q.bindValue(":" + key, value)
        q.exec_()
        q.finish()
        self.close()
