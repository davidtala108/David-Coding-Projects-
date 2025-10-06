class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class Stack:

    def __init__(self, capacity):
        """Creates and empty stack with a capacity"""
        self.capacity = capacity  # Capacity of your stack
        self.head = None  # expect an instance of type Node - This is the starting point of the linked list
        self.num_items = 0  # number of elements in the stack


    def is_empty(self):
        """Returns true if the stack self is empty and false otherwise"""
        return self.num_items == 0

    def is_full(self):
        """Returns true if the stack self is full and false otherwise"""
        return  self.num_items == self.capacity

    def push(self, item):
        """Adds item to the stack"""
        if self.is_full():
            raise IndexError
        N = Node(item)
        if self.head == None:
            self.head = N
        else:
            N.next = self.head
            self.head = N
        self.num_items += 1
    def pop(self):
        """Returns the current top of the stack"""
        if self.is_empty():
            raise IndexError
        item = self.head.item
        self.head = self.head.next
        self.num_items -= 1
        return item

    def peek(self):
        """Returns the value of the item at the top of the stack without removing it"""
        if self.is_empty():
            return None
        return self.head.item

    def size(self):
        """Returns the number of elements currently in the stack, not the capacity"""
        return self.num_items