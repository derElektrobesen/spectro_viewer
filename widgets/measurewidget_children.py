from .measurewidget_parents import *
from PyQt4.QtGui import *

class BlueSpW(MainSpW):
    def __init__(self, parent = None):
        MainSpW.__init__(self, parent)

    def __calculate_graph(self, gr):
        return gr

class RedSpW(MainSpW):
    def __init__(self, parent = None):
        MainSpW.__init__(self, parent)

    def __calculate_graph(self, gr):
        return gr

class OrigBlueSpW(OrigSpW):
    def __init__(self, parent = None):
        OrigSpW.__init__(self, parent)

    def __calculate_graph(self, gr):
        return gr

class OrigRedSpW(OrigSpW):
    def __init__(self, parent = None):
        OrigSpW.__init__(self, parent)

    def __calculate_graph(self, gr):
        return gr

class DiffBlueSpW(DiffSpW):
    def __init__(self, parent = None):
        DiffSpW.__init__(self, parent)

    def __calculate_graph(self, gr):
        return gr

class DiffRedSpW(DiffSpW):
    def __init__(self, parent = None):
        DiffSpW.__init__(self, parent)

    def __calculate_graph(self, gr):
        return gr

class IntactBlueSpW(IntactSpW):
    def __init__(self, parent = None):
        IntactSpW.__init__(self, parent)

    def __calculate_graph(self, gr):
        return gr

class IntactRedSpW(IntactSpW):
    def __init__(self, parent = None):
        IntactSpW.__init__(self, parent)

    def __calculate_graph(self, gr):
        return gr
