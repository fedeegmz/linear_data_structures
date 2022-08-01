from node import TwoWayNode

class DoubleLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.__size__ = 0


    def append(self, data):
        node = TwoWayNode(data)

        if self.tail == None:
            self.tail = node
            self.head = node
        else:
            old_head = self.head
            self.head.set_next(node)
            self.head = node
            self.head.set_previous(old_head)

        self.__size__ += 1
    

    def iter(self):
        current = self.tail

        while current:
            value = current.get_data()
            current = current.get_next()
            yield value


    def search(self, data):
        for node in self.iter():
            if node.get_data() == data:
                print(f'Data: {data} found!')
                return True
        print(f'Data: {data} not found!')
        return False
    

    def delete(self, data):
        for node in self.iter():
            if node.get_data() == data:
                node.get_next().set_previous(node.get_previous())
                node.get_previous().set_next(node.get_next())

                print(f'Data: {data} deleted')
                return True
        
        print(f'Data: {data} not deleted')
        return False


    def clear(self):
        self.head = None
        self.tail = None
        self.__size__ = 0

    
    def size(self):
        return str(self.__size__)