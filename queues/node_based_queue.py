from linked_lists.node import TwoWayNode

class Queue():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.__size__ = 0
    

    def enqueue(self, data):
        node = TwoWayNode(data)

        if self.head == None:
            self.head = node
            self.tail = self.head

        elif self.head == self.tail:
            self.head = node
            self.head.set_next(self.tail)
            self.tail.set_previous(self.head)
        
        else:
            node.set_next(self.head)
            self.head.set_previous(node)
            self.head = node
        self.__size__ += 1
    

    def dequeue(self):
        temporal = self.tail
        
        self.tail = self.tail.get_previous()
        self.tail.set_next(None)
        self.__size__ -= 1

        return temporal.get_data()


    def size(self):
        return str(self.__size__)
    

    def iter(self):
        current = self.tail
        while current:
            value = current.get_data()
            current = current.get_previous()
            yield value
    

    def print(self):
        for data in self.iter():
            print(data)