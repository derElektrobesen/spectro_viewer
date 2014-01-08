from PyQt4.QtGui import *
from .measurewidget_parents import *
from .measurewidget import SpectorsCollection, Params

class BlueCollection(SpectorsCollection):
    def __process_graph_bounds(self, gr):
        return gr

class RedCollection(SpectorsCollection):
    def __process_graph_bounds(self, gr):
        data = gr.get_data()
        new_data = [[], []]
        i = 0
        while data[0][i] <= Params.red_int_stop:
            if data[0][i] >= Params.red_int_stop:
                new_data[0].append(data[0][i])
                new_data[1].append(data[1][i])
        return Graph.from_list(new_data)

class BlueSpW(MainSpW, BlueCollection):
    def __init__(self, parent = None):
        MainSpW.__init__(self, parent)

    def __calculate_graph(self, gr):
        return gr

class RedSpW(MainSpW, RedCollection):
    def __init__(self, parent = None):
        MainSpW.__init__(self, parent)

    def __calculate_graph(self, gr):
        return gr

class OrigBlueSpW(OrigSpW, BlueCollection):
    def __init__(self, parent = None):
        OrigSpW.__init__(self, parent)

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
