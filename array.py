from random import randint

class Array():
    def __init__(self, capacity, fill_value=None):
        self.items = list()
        for _ in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, new_item):
        self.items[index] = new_item

    def __sumall__(self):
        result = 0
        for elem in self.items:
            result += elem
        return result

    def __randitems__(self):
        for index in range(len(self.items)):
            self.items[index] = randint(0, 100)