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

class __Params:
    @_st_prop
    def red_int_start(): return 6600.0

    @_st_prop
    def red_int_end(): return 8000.0

    @_st_prop
    def a1_start(): return 6650.0

    @_st_prop
    def a1_end(): return 6750.0

    @_st_prop
    def a2_start(): return 6950.0

    @_st_prop
    def a2_end(): return 7050.0

class SpectorsCollection:
    def __init__(self):
        self.__graphs = {}

    def add_graph(self, key, graph):
        graph = self.__process_graph_bounds(graph)
        self.__graphs[key] = { 'graph': graph, }

    def remove_graph(self, key):
        del self.__graphs[key]

    def clear(self):
        self.__graphs = {}

    def set_graph(self, key, graph):
        self.clear()
        self.add_graph(key, graph)

    def graphs(self):
        return self.__graphs

    def __process_graph_bounds(self, gr):
        return gr

class MeasureWidget(FigureCanvas, SpectorsCollection):
    def __init__(self, parent = None):
        self.__fig = Figure()
        self.__axes = self.__fig.add_subplot(111)
        FigureCanvas.__init__(self, self.__fig)
        self.setParent(parent)

    def set_color(self, key, color):
        if key in self.graphs():
            self.__graph[key]['color'] = color

    def __calculate_graph(self, gr):
        return gr   # virtual method

    def render(self):
        plt = self.__axes
        plt.cla()
        for gr in self.graphs().values():
            line = plt.plot(*(gr['graph'].get_data()))
            if 'color' in gr:
                plt.setp(line, color = gr['color'])
        self.__fig.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
        self.draw()
