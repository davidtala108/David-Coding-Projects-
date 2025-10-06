
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class QueuekLinkedList:
    """Implements an efficient first-in first-out Abstract Data Type using a linked List"""

    def __init__(self, capacity):
        """Creates and empty queue with a capacity"""
        self.capacity = capacity  # Capacity of your queue
        self.head = None  # expect an instance of type Node - This is the starting point of the linked list
        self.tail = None
        self.num_items = 0  # number of elements in the queue

    def is_empty(self):
        """Returns true if the queue self is empty and false otherwise"""
        return  self.num_items == 0
    def is_full(self):
        """Returns true if the queue self is full and false otherwise"""
        return self.num_items == self.capacity
    def enqueue(self, item):
        """Adds item to the queue"""
        if self.is_full():
            raise IndexError
        N = Node(item)
        if self.is_empty():
          self.head = N
          self.tail = N
          self.head.next = self.tail
        else:
          self.tail.next = N
          self.tail = N
        self.num_items += 1
    def dequeue(self):
        """Returns the current front of the queue"""
        if self.is_empty():
            raise IndexError
        item = self.head.item
        self.head = self.head.next
        self.num_items -= 1
        return item

    def peek(self):
        """Returns the value of the item at the front of the queue without removing it"""
        return self.head.item
    def size(self):
        """Returns the number of elements currently in the queue, not the capacity"""
        return self.num_items