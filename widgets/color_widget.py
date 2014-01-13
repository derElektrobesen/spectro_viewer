from PyQt4.QtGui import QWidget, QPainter, QBrush, QPen, QColor, QColorDialog
from PyQt4.QtCore import Qt, QRect
from settings import Settings

class ColorWidget(QWidget):
    def __init__(self, parent = None, color = "#000000"):
        QWidget.__init__(self, parent)
        self.set_color(color)
        self.setFixedHeight(20)
        self.__on_color_change = None

    def set_color(self, color):
        if color:
            self.__color = QColor()
            self.__color.setNamedColor(color)

    def on_color_change(self, f):
        self.__on_color_change = f

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(self.__color))
        b = QBrush(Qt.SolidPattern)
        b.setColor(self.__color)
        painter.setBrush(b)
        painter.drawRect(QRect(0, 0, self.width() - 1, self.height() - 1))

    def mousePressEvent(self, e):
        c = QColorDialog.getColor(self.__color)
        self.__color = c
        self.repaint()
        name = c.name()
        if self.__on_color_change:
            self.__on_color_change(name)
        if name not in Settings.colors:
            Settings.colors.append(name)
            Settings.store()
