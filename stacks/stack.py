from linked_lists.node import Node

class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.__size__ = 0
    

    def peek(self):
        if self.top:
            return self.top.get_data()
        elif self.bottom:
            return self.bottom.get_data()
        else:
            return "The stack is empty"
    

    def push(self, data):
        node = Node(data)

        if self.bottom == None:
            self.bottom = node
            self.top = node
        elif self.top == None:
            self.top = node
            self.top.set_next(self.bottom)
        else:
            node.set_next(self.top)
            self.top = node
        
        self.__size__ += 1
    

    def pop(self):
        if self.top:
            temporal = self.top
            self.top = self.top.get_next()
            self.__size__ -= 1
            return temporal.get_data()
        
        elif self.bottom:
            temporal = self.bottom
            self.bottom = None
            self.__size__ = 0
            return temporal.get_data()

        else:
            return "The stack is empty"
    

    def size(self) -> str:
        return str(self.__size__)
    

    def search(self, data):
        for node in self.iter():
            if node == data:
                print(f'Data: {data} found!')
                return True
        print(f'Data: {data} not found!')
        return False
    

    def delete(self, data):
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
        self.top = None
        self.bottom = None
        self.__size__ = 0


    def iter(self):
        current = self.top

        while current:
            value = current.get_data()
            current = current.get_next()
            yield value
    

    def __iter_node__(self) -> Node:
        current = self.top

        while current:
            node = current
            current = current.get_next()
            yield node