class ListQueue():
    def __init__(self) -> None:
        self.items = []
        self.__size__ = len(self.items)


    def enqueue(self, data):
        self.items.insert(0, data)
        self.__size__ += 1
    

    def dequeue(self):
        data = self.items.pop()
        self.__size__ -= 1
        return data
    

    def size(self):
        return str(self.__size__)
    

    def iter(self):
        index = 0
        current = self.items[index]
        while index < self.__size__:
            index += 1
            value = current
            current = self.items[index]
            yield value
    

    def traverse(self):
        for item in self.items:
            print(item)