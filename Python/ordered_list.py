class Node:
    '''Node for use with doubly-linked list'''

    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           DO NOT have an attribute to keep track of size'''
        self.head = None

    def is_empty(self):
        '''Returns True if OrderedList is empty
            MUST have O(1) performance'''
        return self.head is None

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head end of list) to highest (at tail end of list) and returns True.
           If the item is already in the list, do not add it again and return False.
           MUST have O(n) average-case performance.  Assume that all items added to your
           list can be compared using the < operator and can be compared for equality/inequality.
           Make no other assumptions about the items in your list'''
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            return True
        current = self.head
        prev = None
        while current is not None and current.item < item:
            prev = current
            current = current.next
        if current is not None and current.item == item:
            return False
        new_node.prev = prev
        new_node.next = current
        if prev is None:
            self.head = new_node
        else:
            prev.next = new_node
        if current is not None:
            current.prev = new_node
        return True

    def remove(self, item):
        '''Removes the first occurrence of an item from OrderedList. If item is removed (was in the list)
           returns True.  If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        current = self.head
        while current is not None:
            if current.item == item:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return True
            current = current.next
        return False

    def index(self, item):
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        index = 0
        current = self.head
        while current is not None:
            if current.item == item:
                return index
            current = current.next
            index += 1
        return None

    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        if index < 0:
            raise IndexError("Index out of range")

        current = self.head
        for i in range(index):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next

        if current is None:
            raise IndexError("Index out of range")

        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next
        if current.next:
            current.next.prev = current.prev

        return current.item

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        return self._search_recursive(item, self.head)

    def _search_recursive(self, item, current):
        if current is None:
            return False
        if current.item == item:
            return True
        return self._search_recursive(item, current.next)

    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        result = []
        current = self.head
        while current is not None:
            result.append(current.item)
            current = current.next
        return result

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        return self._python_list_reversed_recursive(self.head)

    def _python_list_reversed_recursive(self, current):
        if current is None:
            return []
        return self._python_list_reversed_recursive(current.next) + [current.item]

    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        return self._size_recursive(self.head)

    def _size_recursive(self, current):
        if current is None:
            return 0
        return 1 + self._size_recursive(current.next)

