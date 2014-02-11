from PyQt4.QtGui import *
from .measurewidget_parents import *
from .measurewidget import SpectorsCollection, Params
from pr_core import Graph

class BlueCollection(SpectorsCollection):
    def __process_graph_bounds(self, gr):
        return gr

class RedCollection(SpectorsCollection):
    def process_graph_bounds(self, gr):
        data = gr.get_data()
        new_data = [[], []]
        i = 0
        i_s = gr.search_index(Params.red_int_start)
        i_e = gr.search_index(Params.red_int_end)

        if i_s == None:
            i_s = 0
        if i_e == None:
            i_e = len(data[0]) - 1

        new_data[0] = data[0][i_s:i_e + 1]
        new_data[1] = data[1][i_s:i_e + 1]
        return Graph.from_list(new_data)

class BlueSpW(MainSpW, BlueCollection):
    def __init__(self, parent = None):
        MainSpW.__init__(self, parent)

    def __calculate_graph(self, gr):
        return gr

class OrigBlueSpW(OrigSpW, BlueCollection):
    def __init__(self, parent = None):
        OrigSpW.__init__(self, parent)
        self.__ia = {}
        self.__s = {}

    def __calculate_graph(self, gr):
        return gr

    def get_ia(self):
        graphs = self.graphs()
        def f(gr, min_y):
            a = gr.count_s(Params.a1_start, Params.a1_end, min_y = min_y)
            b = gr.count_s(Params.a2_start, Params.a2_end, min_y = min_y)
            return a / b

        for key, val in graphs.items():
            if key not in self.__ia:
                m = min(val['graph'].get_data()[1])
                self.__ia[key] = f(val['graph'], m)
        return self.__ia

    def get_s(self):
        graphs = self.graphs()
        def f(gr):
            return gr.count_s()
        for key, val in graphs.items():
            if key not in self.__s:
                self.__s[key] = f(val['graph'])
        return self.__s

class RedSpW(MainSpW, RedCollection):
    def __init__(self, parent = None):
        MainSpW.__init__(self, parent)

    def __calculate_graph(self, gr):
        return gr

class OrigRedSpW(OrigSpW, RedCollection):
    def __init__(self, parent = None):
        OrigSpW.__init__(self, parent)

    def __calculate_graph(self, gr):
        return gr

class DiffBlueSpW(DiffSpW, BlueCollection):
    def __init__(self, parent = None):
        DiffSpW.__init__(self, parent)

    def __calculate_graph(self, gr):
        return gr

class DiffRedSpW(DiffSpW, RedCollection):
    def __init__(self, parent = None):
        DiffSpW.__init__(self, parent)

    def __calculate_graph(self, gr):
        return gr

class IntactBlueSpW(IntactSpW, BlueCollection):
    def __init__(self, parent = None):
        IntactSpW.__init__(self, parent)

    def __calculate_graph(self, gr):
        return gr

class IntactRedSpW(IntactSpW, RedCollection):
    def __init__(self, parent = None):
        IntactSpW.__init__(self, parent)

    def __calculate_graph(self, gr):
        return gr
