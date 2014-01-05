#!/usr/bin/python3
# encoding: utf-8

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from db import MySQL
from PyQt4.QtGui import *
from forms import MainWindow

if __name__ == "__main__":
    sql_con = MySQL('root', 'tashkent')
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    app.exec_()
    sql_con.close_connection()
