class Graph:
    def __init__(self, dev_data = None):
        self.__data = None
        if dev_data:
            self.compile_dev_data(dev_data)

    def compile_dev_data(self, data):
        data = list(map(float, data.decode('utf-8').split()))
        self.__data = list(zip(data[0::2], data[1::2]))

    def get_data(self):
        return self.__data

    def __str__(self):
        return str(self.__data)
