from .measurewidget import MeasureWidget, SpectorsCollection, Params
from pr_core import Graph
from PyQt4.QtGui import *

class MainSpW(MeasureWidget, SpectorsCollection):
    def __init__(self, parent = None):
        MeasureWidget.__init__(self, parent)
        SpectorsCollection.__init__(self)

    def __normalize(self, gr):
        data = gr.get_data()
        delta = data[0][1] - data[0][0]
        offset = int(Params.normalize_offset / delta)
        delta = int(Params.normalize_step / delta)

        r = [[],[]]

        j = offset
        i = offset
        min_y = min(data[1])
        full_s = gr.count_s(min_y = min_y, stop = Params.normalize_right_border)

        while (i < len(data[1])):
            i += delta
            if i >= len(data[1]) or data[0][i] > Params.normalize_right_border:
                break
            s = gr.count_s(start_index = j, stop_index = i, min_y = min_y)
            r[1].append(full_s / s)
            r[0].append(0.5 * (data[0][i] + data[0][j]))
            j += delta

        return Graph.from_list(r)

    def process_graph_data(self, gr):
        return self.__normalize(gr)

class OrigSpW(MeasureWidget, SpectorsCollection):
    def __init__(self, parent = None):
        MeasureWidget.__init__(self, parent)
        SpectorsCollection.__init__(self)

    def process_graph_data(self, gr):
        return gr

class DiffSpW(MainSpW):
    def __init__(self, parent = None):
        MainSpW.__init__(self)

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
        gr = super().process_graph_data(gr)
        return self.__differ(gr)

class IntactSpW(MeasureWidget, SpectorsCollection):
    def __init__(self, parent = None):
        MeasureWidget.__init__(self, parent)
        SpectorsCollection.__init__(self)

    def process_graph_data(self, gr):
        return gr
