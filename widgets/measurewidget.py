from PyQt4.QtGui import *
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.legend_handler import HandlerLine2D
from matplotlib.lines import Line2D

class MeasureWidget(FigureCanvas):
    def __init__(self, parent = None):
        self.__fig = Figure()
        self.__axes = self.__fig.add_subplot(111)
        FigureCanvas.__init__(self, self.__fig)
        self.setParent(parent)

    def render(self, fig_1, fig_2):
        #self.__axes.cla()
        #self.__axes.plot(*zip(*fig_1), label='Original func')
        #self.__axes.plot(*zip(*fig_2), label='Generated func')
        #my_handler = HandlerLine2D(numpoints=1)
        #legend = self.__axes.legend(handler_map={Line2D:my_handler})
        #for label in legend.get_texts():
        #    label.set_fontsize('small')
        #self.draw()
        pass
