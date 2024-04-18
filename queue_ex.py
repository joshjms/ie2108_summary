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
        # .pop(0) takes O(N) time
        return self.items.pop(0) # .pop(0) removes the first element
    def size(self):
        # Returns the size of the queue
        return len(self.items)

# .pop() in Python takes O(1) to remove the last element and O(N) to remove the first 
# element. This is due to the implementation and memory addressing of Python list.