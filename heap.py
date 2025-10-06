
class MaxHeap:

    def __init__(self, capacity=50):
        '''Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created.'''
        self.capacity = capacity
        self.root= [None] * (capacity + 1)
        self.size = 0

    def enqueue(self, item):
        '''inserts "item" into the heap, returns true if successful, false if there is no room in the heap
           "item" can be any primitive or ***object*** that can be compared with other
           items using the < operator'''
        if self.is_full():
            return False
        if self.is_empty():
            self.root[self.size + 1] = item
            self.size += 1
            return True
        self.root[self.size + 1] = item
        self.size += 1
        return self.perc_up(self.size)


        # Should call perc_up


    def peek(self):
        '''returns max without changing the heap, returns None if the heap is empty'''
        if self.is_empty():
            return None
        return self.root[1]

    def dequeue(self):
        '''returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty'''
        if self.is_empty():
            return None
        Max = self.root[1]
        self.root[1] = self.root[self.size]
        self.root[self.size] = None
        self.size -= 1
        self.perc_down(1)
        return Max
        # Should call perc_down


    def contents(self):
        '''returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)'''
        return self.root[1:self.size + 1]

    def build_heap(self, alist):
        '''Discards all items in the current heap and builds a heap from
        the items in alist using the bottom-up construction method.
        If the capacity of the current heap is less than the number of
        items in alist, the capacity of the heap will be increased to accommodate
        exactly the number of items in alist'''
        size = len(alist)
        if size > self.capacity:
            self.capacity = size
            self.root = [None] * (self.capacity + 1)
        for i in range(1, size + 1):
            self.root[i] = alist[i-1]
            self.size += 1
        for j in range(0,size,2):
            Sort_index = (size - j)//2
            if Sort_index == 0:
                break
            self.perc_down(Sort_index)

        # Bottom-Up construction.  Do NOT call enqueue


    def is_empty(self):
        '''returns True if the heap is empty, false otherwise'''
        return self.get_size() == 0

    def is_full(self):
        '''returns True if the heap is full, false otherwise'''
        return self.get_size() == self.capacity

    def get_capacity(self):
        '''this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold'''
        return self.capacity

    def get_size(self):
        '''the actual number of elements in the heap, not the capacity'''
        return self.size

    def perc_down(self, i):
        '''where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        left_child = 2 * i
        right_child = 2 * i + 1
        if left_child > self.capacity or right_child > self.capacity:
            return
        max_child = left_child
        if (self.root[right_child] != None and
                self.root[right_child] > self.root[left_child]):
            max_child = right_child

        if self.root[max_child] != None and self.root[max_child] > self.root[i]:
            self.root[i], self.root[max_child] = self.root[max_child], self.root[i]
            self.perc_down(max_child)
        return

    def perc_up(self, i):
        '''where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        parent = (i // 2)
        if self.root[parent] != None:
            if self.root[i] > self.root[parent]:
                temp = self.root[parent]
                self.root[parent] = self.root[i]
                self.root[i] = temp
                self.perc_up(parent)
                return True
            else:
                return True
        else:
            return True

    def heap_sort_ascending(self, alist):
        '''perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order'''
        self.build_heap(alist)
        size = len(alist)
        for i in range(size):
            alist[size-1-i]=  self.dequeue()
        return alist
