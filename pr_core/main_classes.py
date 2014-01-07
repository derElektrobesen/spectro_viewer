class Graph:
    def __init__(self, dev_data = None, data = None):
        self.__data = data
        if dev_data:
            self.compile_dev_data(dev_data)

    def compile_dev_data(self, data):
        data = tuple(map(float, data.decode('utf-8').split()))
        self.__data = (data[0::2], data[1::2])

    def get_data(self):
        return self.__data

    def __str__(self):
        return str(self.__data)

    def copy(self):
        return Graph(data = tuple(self.__data))

    def __concat__(self, gr):
        def add(x, y): return x + y
        def f(arr_1, arr_2): return tuple(map(add, arr_1, arr_2))
        return Graph(data = (f(self.__graph[0], gr[0]), f(self.__graph[1], gr[1])))

    def __truediv__(self, num):
        def f(arr): return tuple(map(lambda x: x / num, arr))
        return Graph(data = (f(self.__graph[0]), f(self.__graph[1])))

    def __iadd__(self, gr):
        self.__data = (self + gr).get_data()
        return self

    def __idiv__(self, num):
        self.__data = (self / num).get_data()
        return self

class GraphCollection:
    def __init__(self):
        self.__graphs = []
        self.__to_remove = []

    def add_graph(self, gr):
        self.__graphs.insert(0, gr)
        return self

    def remove_graph_deffered(self, index):
        self.__to_remove.append(index)
        return self

    def remove_deffered_graphs(self):
        for index in self.__to_remove:
            self.remove_graph(index)
        return self

    def remove_graph(self, index):
        self.__graphs.pop(index)
        return self

    def get_graph(self, index):
        return self.__graphs[index]

    def average_graphs(self):
        r = None
        for gr in self.__graphs:
            if not r:
                r = gr
            else:
                r += gr
        r /= len(self.__graphs)
        return r

    def count(self):
        return len(self.__graphs)

    def empty(self):
        return self.count() == 0

    def __iter__(self):
        return self.__graphs.__iter__()

class MeasureCollection:
    def __init__(self):
        self.__measures = []

    def add_measure(self, m):
        self.__measures.insert(0, m)
        return self

    def remove_measure(self, index):
        self.__measures.pop(index)
        return self

    def get_measure(self, index):
        return self.__measures[index]

    def set_measure(self, index, measure):
        self.__measures[index] = measure
        return self

    def count(self):
        return len(self.__measures)

    def empty(self):
        return self.count() == 0

    def add_to_measure(self, index, graph):
        self.__measures[index].add_graph(graph)
        return self

    def add_graph(self, gr):
        return self.add_to_measure(0, gr)

    def init_collection(self):
        return self.add_measure(GraphCollection())

    def __iter__(self):
        return self.__measures.__iter__()
