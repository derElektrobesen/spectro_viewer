#!/usr/bin/python3
# encoding: utf-8

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from PyQt4.QtGui import *
from forms import MainWindow

if __NAME__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    app._exec()
