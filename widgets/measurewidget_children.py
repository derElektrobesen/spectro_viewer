from PyQt4.QtGui import *
from .measurewidget_parents import *
from .measurewidget import SpectorsCollection

class BlueCollection(SpectorsCollection):
    def __process_graph_bounds(self, gr):
        print("Blue")
        return gr

class RedCollection(SpectorsCollection):
    def __process_graph_bounds(self, gr):
        print("Red")
        return gr

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
