from stacks.stack import Stack

class Queue():
    def __init__(self) -> None:
        self.inbound_stack = []
        self.outbound_stack = []
    

    def enqueue(self, data):
        self.inbound_stack.append(data)
    

    def dequeue(self):
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())

        return self.outbound_stack.pop()


class StackQueue():
    def __init__(self) -> None:
        self.inbound_stack = Stack()
        self.outbound_stack = Stack()

    
    def enqueue(self, data):
        self.inbound_stack.push(data)
    

    def dequeue(self):
        if self.outbound_stack.__size__ == 0:
            for data in self.inbound_stack.iter():
                self.outbound_stack.push(data)
            self.inbound_stack.clear()
        
        return self.outbound_stack.pop()