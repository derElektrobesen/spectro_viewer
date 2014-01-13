from PyQt4.QtGui import QWidget, QPainter, QBrush, QPen, QColor
from PyQt4.QtCore import Qt, QRect

class ColorWidget(QWidget):
    def __init__(self, parent = None, color = "#000000"):
        QWidget.__init__(self, parent)
        self.set_color(color)
        self.setFixedHeight(20)

    def set_color(self, color):
        if color:
            self.__color = QColor()
            self.__color.setNamedColor(color)

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(self.__color))
        b = QBrush(Qt.SolidPattern)
        b.setColor(self.__color)
        painter.setBrush(b)
        painter.drawRect(QRect(0, 0, self.width() - 1, self.height() - 1))
