# Stack implementation in Python

class Stack:
    def __init__(self): 
        # Initializes the stack as a list
        self.items = []
    def push(self, item):
        # Adds an item to the stack
        self.items.append(item)
    def pop(self):
        # Removes an item from the stack and returns it 
        # (Note that stack takes the top-most element)
        return self.items.pop()
    def peek(self):
        # Returns the top-most element of the stack
        return self.items[-1]
    def size(self):
        # Returns the size of the stack
        return len(self.items)
    
class Queue:
    def __init__(self):
        # Initializes the queue as a list
        self.items = []
    def enqueue(self, item):
        # Adds an item to the queue
        self.items.append(item)
    def dequeue(self):
        # Removes an item from the queue and returns it
        # (Note that queue takes the front-most element)
        return self.items.pop(0) # .pop(0) removes the first element
    def size(self):
        # Returns the size of the queue
        return len(self.items)
