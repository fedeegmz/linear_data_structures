from linked_lists.node import Node

class Stack():
    def __init__(self):
        self.top = None
        self.__size__ = 0
    

    def peek(self):
        """ Returns the las node of the stack """
        if self.top:
            return self.top.get_data()
        else:
            return None
    

    def bottom(self):
        """ Returns the first node of the stack """
        current = None
        for data in self.iter():
            current = data
        return current
    

    def push(self, data):
        """
            Add a node to the stack
            - Param:
                - data: node data to add
        """
        node = Node(data)

        if self.top == None:
            self.top = node
        else:
            node.set_next(self.top)
            self.top = node
        
        self.__size__ += 1
    

    def pop(self):
        """
            Remove the last node from the stack
            - Return:
                - node.get_data():  node data to delete
        """
        if self.top:
            temporal = self.top
            self.top = self.top.get_next()
            self.__size__ -= 1
            return temporal.get_data()
        
        else:
            self.clear()
            return None
    

    def size(self) -> str:
        """ Returns the size of the stack """
        return str(self.__size__)
    

    def search(self, data):
        """
            Returns true if the data exist on the stack
            - Param:
                - data: node data to search
            - Returns:
                - True: if the data exist
                - False: if the data does not exist
        """
        for node in self.iter():
            if node == data:
                print(f'Data: {data} found!')
                return True
        print(f'Data: {data} not found!')
        return False
    

    def delete(self, data):
        """
            Remove the data from a node if it exist on the stack
            - Param:
                - data: data to delete
        """
        if data == self.peek():
            self.pop()
        else:
            current = None
            previous = None
            for node in self.__iter_node__():
                previous = current
                current = node
                if current.get_data() == data:
                    previous.set_next(current.get_next())
                    return current.get_data()
    

    def clear(self):
        """ Empty the stack """
        self.top = None
        self.__size__ = 0


    def iter(self):
        """ Returns the data of the nodes one by one, from the last to the first """
        current = self.top

        while current:
            value = current.get_data()
            current = current.get_next()
            yield value
    

    def __iter_node__(self) -> Node:
        """ Returns the nodes one by one, from the last to the first """
        current = self.top

        while current:
            node = current
            current = current.get_next()
            yield node