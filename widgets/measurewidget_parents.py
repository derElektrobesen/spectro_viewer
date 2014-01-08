from .measurewidget import MeasureWidget, SpectorsCollection, Params
from pr_core import Graph
from PyQt4.QtGui import *

class MainSpW(MeasureWidget, SpectorsCollection):
    def __init__(self, parent = None):
        MeasureWidget.__init__(self, parent)
        SpectorsCollection.__init__(self)

    def process_graph_data(self, gr):
        return gr

class OrigSpW(MeasureWidget, SpectorsCollection):
    def __init__(self, parent = None):
        MeasureWidget.__init__(self, parent)
        SpectorsCollection.__init__(self)

    def process_graph_data(self, gr):
        return gr

class DiffSpW(MeasureWidget, SpectorsCollection):
    def __init__(self, parent = None):
        MeasureWidget.__init__(self, parent)
        SpectorsCollection.__init__(self)

    def __differ(self, gr):
        new_data = [[], []]
        data = gr.get_data()
        wnd = Params.diff_window

        if len(gr) < wnd:
            return gr
        for i in range(wnd, len(gr), wnd):
            dx = data[0][i] - data[0][i - wnd]
            dy = data[1][i] - data[1][i - wnd]
            new_data[0].append(data[0][i] + dx / 2.0)
            new_data[1].append(dy / dx)
        return Graph.from_list(new_data)

    def process_graph_data(self, gr):
        return self.__differ(gr)

class IntactSpW(MeasureWidget, SpectorsCollection):
    def __init__(self, parent = None):
        MeasureWidget.__init__(self, parent)
        SpectorsCollection.__init__(self)

    def process_graph_data(self, gr):
        return gr
