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
        self.__graph = f(self.__graph[0], gr[0]), f(self.__graph[1], gr[1])
        return self

    def __truediv__(self, num):
        def f(arr): return tuple(map(lambda x: x / num, arr))
        self.__graph = f(self.__graph[0]), f(self.__graph[1])
        return self

class GraphCollection:
    def __init__(self):
        self.__graphs = []

    def add_graph(self, gr):
        self.__graph.insert(0, gr)

    def get_graph(self, index):
        return self.__graph[index]
