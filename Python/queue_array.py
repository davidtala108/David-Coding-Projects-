class QueueArray:
    """Implements an efficient first-in first-out Abstract Data Type using a Python List"""

    def __init__(self, capacity):
        """Creates an empty queue with a capacity"""
        self.capacity = capacity  # Capacity of your queue
        self.items = [None] * capacity  # initializing the queue
        self.Back = 0
        self.Front = 0
        self.num_items = 0  # number of elements in the queue

    def is_empty(self):
        """Returns true if the queue self is empty and false otherwise"""
        return self.num_items == 0
    def is_full(self):
        """Returns true if the queue self is full and false otherwise"""
        return self.num_items == self.capacity
    def enqueue(self, item):
        """Adds item to the queue"""
        if self.is_full():
            raise IndexError

        self.items[self.Front] = item
        self.Front += 1
        if self.Front == self.capacity:
            self.Front = 0
        self.num_items += 1
    def dequeue(self):
        """Returns the current front of the queue"""
        if self.is_empty():
            raise IndexError
        item = self.items[self.Back]
        self.Back += 1
        if self.Back == self.capacity:
            self.Back = 0
        self.num_items -= 1
        return item
    def peek(self):
        """Returns the value of the item at the front of the queue without removing it"""
        return self.items[self.Back]
    def size(self):
        """Returns the number of elements currently in the queue, not the capacity"""
        return self.num_items