from typing import List
from linked_lists.node import TwoWayNode

class Queue():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.__size__ = 0
    

    def enqueue(self, data):
        """
            Add a node to the queue

            - Param:
                - node: node to add
        """

        node = TwoWayNode(data)

        if self.head == None:
            self.head = node
            self.head.set_previous(None)
            self.tail = self.head
            self.tail.set_next(None)
        
        elif self.head == self.tail:
            self.head = node
            self.head.set_previous(None)
            self.head.set_next(self.tail)
            self.tail.set_previous(self.head)
            self.tail.set_next(None)
        
        else:
            node.set_next(self.head)
            self.head.set_previous(node)
            self.head = node
            self.head.set_previous(None)
        
        self.__size__ += 1
    

    def dequeue(self):
        """
            Remove the first node from the queue

            - Return:
                - node.get_data():  the data of the first node
        """

        if self.__size__ > 0:
            temporal = self.tail
            
            if self.head == self.tail:
                self.clear()
            
            else:
                self.tail = self.tail.get_previous()
                self.tail.set_next(None)
                self.__size__ -= 1
            
            return temporal.get_data()


    def size(self) -> str:
        """ Returns the size of the queue """

        return str(self.__size__)
    

    def iter(self):
        """ Returns the data of the nodes one by one, from the first to the last """

        current = self.tail
        while current:
            value = current.get_data()
            current = current.get_previous()
            yield value
    

    def __iterNode__(self):
        """ Returns the nodes one by one, from the first to the last """

        current = self.tail
        while current:
            value = current
            current = current.get_previous()
            yield value

    
    def remove(self, data):
        """
            Remove a node from the queue

            - Param:
                - data: node data to delete
        """

        if data == self.head.get_data():
            self.head = self.head.get_next()
            self.head.set_previous(None)
        
        elif data == self.tail.get_data():
            self.pop()
        
        else:
            for node in self.__iterNode__():
                if node.get_data() == data:
                    node.get_previous().set_next(node.get_next())
                    node.get_next().set_previous(node.get_previous())
    

    def clear(self):
        """ Empty the queue """

        self.head = None
        self.tail = None
        self.__size__ = 0
    

    def to_list(self) -> List:
        """ Returns a list with the data of the nodes in the queue """

        new_list = []
        for data in self.iter():
            new_list.append(data)
        
        return new_list


    def print(self):
        """ Print the data of the all nodes """
        for data in self.iter():
            print(data)