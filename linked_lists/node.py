class Node():
    def __init__(self, data, next=None):
        self.__data__ = data
        self.__next__ = next


    def set_next(self, node):
        try:
            self.__next__ = node
        except:
            print("ERROR: No se pudo setear el nodo")
            return False
        else:
            return True
    

    def get_next(self):
        return self.__next__


    def set_data(self, new_data):
        try:
            self.__data__ = new_data
        except:
            print("ERROR: No se pudo setear data")
            return False
        else:
            return True


    def get_data(self):
        return self.__data__


class TwoWayNode(Node):
    def __init__(self, data, previous=None, next=None):
        super().__init__(data, next)
        self.__previous__ = previous
    

    def set_previous(self, node):
        try:
            self.__previous__ = node
        except:
            print("ERROR: No se pudo setear el nodo")
            return False
        else:
            return True
    

    def get_previous(self):
        return self.__previous__