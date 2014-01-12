import numpy as np
from PyQt4.QtGui import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.legend_handler import HandlerLine2D
from matplotlib.lines import Line2D

def _composed(*decs):
    def deco(f):
        for dec in reversed(decs):
            f = dec(f)
        return f
    return deco

_st_prop = _composed(staticmethod, property)

class Params:
    red_int_start = 6600.0
    red_int_end = 8000.0
    a1_start = 6650.0
    a1_end = 6750.0
    a2_start = 6950.0
    a2_end = 7050.0
    normalize_step = 10
    normalize_offset = 60.0
    normalize_right_border = 8700.0
    diff_window = 5

class SpectorsCollection:
    def __init__(self):
        self.__graphs = {}

    def add_graph(self, key, graph):
        graph = self.process_graph_bounds(graph)
        graph = self.process_graph_data(graph)

        d = graph.get_data()
        self.__graphs[key] = { 'graph': graph, }

    def remove_graph(self, key):
        del self.__graphs[key]

    def clear(self):
        self.__graphs = {}

    def set_graph(self, key, graph):
        self.clear()
        self.add_graph(key, graph)

    def get_graph(self, key):
        return self.__graphs[key]['graph'] if key in self.__graphs else None

    def graphs(self):
        return self.__graphs

    def process_graph_bounds(self, gr):
        return gr

    def process_graph_data(self, gr):
        return gr

class MeasureWidget(FigureCanvas, SpectorsCollection):
    def __init__(self, parent = None):
        self.__fig = Figure()
        FigureCanvas.__init__(self, self.__fig)
        SpectorsCollection.__init__(self)
        self.__axes = self.__fig.add_subplot(111)
        self.setParent(parent)

    def set_color(self, key, color):
        if key in self.graphs():
            self.__graph[key]['color'] = color

    def render(self):
        plt = self.__axes
        plt.cla()
        xmin, xmax = 99999999, -1
        for gr in self.graphs().values():
            data = gr['graph'].get_data()
            if data[0][0] < xmin:
                xmin = data[0][0]
            if data[0][-1] > xmax:
                xmax = data[0][-1]
            line = plt.plot(*data)
            if 'color' in gr:
                plt.setp(line, color = gr['color'])
        plt.set_xlim(xmin, xmax)
        self.__fig.subplots_adjust(left=0.07, right=0.95, top=0.9, bottom=0.1)
        self.draw()
