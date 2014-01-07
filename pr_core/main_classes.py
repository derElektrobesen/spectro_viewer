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

class GraphCollection:
    def __init__(self):
        self.__graphs = []
