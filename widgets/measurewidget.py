import numpy as np
from PyQt4.QtGui import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.legend_handler import HandlerLine2D
from matplotlib.lines import Line2D

class MeasureWidget(FigureCanvas):
    def __init__(self, parent = None):
        self.__fig = Figure()
        self.__axes = self.__fig.add_subplot(111)
        self.__graphs = {}
        FigureCanvas.__init__(self, self.__fig)
        self.setParent(parent)

    def add_graph(self, key, graph):
        self.__graphs[key] = { 'graph': graph, }

    def set_graph(self, key, graph):
        self.clear()
        self.add_graph(key, graph)

    def remove_graph(self, key):
        del self.__graphs[key]

    def clear(self):
        self.__graphs = {}

    def set_color(self, key, color):
        if key in self.__graph:
            self.__graph[key]['color'] = color

    def render(self):
        plt = self.__axes
        plt.cla()
        for gr in self.__graphs.values():
            line = plt.plot(*zip(*(gr['graph'].get_data())))
            if 'color' in gr:
                plt.setp(line, color = gr['color'])
        self.__fig.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
        self.draw()
