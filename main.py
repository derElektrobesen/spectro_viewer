#!/usr/bin/python3
# encoding: utf-8

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from PyQt4.QtGui import *
from db import MySQL, SqlException
from forms import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    wnd = MainWindow()
    act = QAction("DB_connected", wnd)
    act.triggered.connect(wnd.load_database)
    wnd.show()
    sql_con = MySQL('root', 'tashkent', act)
    app.exec_()
    sql_con.close_connection()
