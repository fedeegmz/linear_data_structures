from node import Node

class SinglyLinkedList():
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.__size__ = 0


    def append(self, data):
        node = Node(data)

        if self.tail == None:
            self.tail = node
            self.head = node
        else:
            self.head.set_next(node)
            self.head = node

        self.__size__ += 1


    def size(self):
        return str(self.__size__)


    def iter(self):
        current = self.tail

        while current:
            value = current.get_data()
            current = current.get_next()
            yield value


    def delete(self, data):
        current = self.tail
        previus = self.tail

        while current:
            if current.get_data() == data:
                if current == self.tail:
                    self.tail = current.get_next()
                else:
                    if not previus.set_next(current.get_next()):
                        print("No se pudo eliminar")
                
                self.__size__ -= 1
                return current.get_data()

            previus = current
            current = current.get_next()


    def search(self, data):
        for node in self.iter():
            if data == node:
                print(f'Data {data} found!')
                return True
        
        print(f'Data {data} not found!')
        return False


    def clear(self):
        self.tail = None
        self.head = None
        self.__size__ = 0

