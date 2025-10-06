class BinHeap:
    class MyException(Exception):
        pass
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.num_items = 0

    def __repr__(self):
        string = []
        for i in range(len(self.array)):
            if self.array[i + 1] == None:
                break
            else:
                string.append(str(self.array[i + 1]))
        string2 = ' '.join(string)
        return string2

    def isEmpty(self):
        return self.num_items == 0
    def size(self):
        return self.num_items
    def insert(self,Any):
        if self.size() + 1 == self.capacity:
            temp = []
            for val in self.array:
                temp.append(val)
            self.capacity *= 2
            self.array = [None] * self.capacity
            self.num_items = 0
            for i in range(1,len(temp)):
                self.array[self.num_items + 1] = temp[i]
                self.num_items += 1
        self.array[self.num_items + 1] = Any
        Index = self.num_items + 1
        while True:
            if Index // 2 != 0:
                if self.array[Index // 2] > self.array[Index]:
                    temp = self.array[(Index) // 2]
                    self.array[Index // 2] = self.array[Index]
                    self.array[Index] = temp
                    Index = Index // 2
                else:
                    break
            else:
                break
        self.num_items += 1
    def deleteMin(self):
        if self.isEmpty():
            raise self.MyException("Heap is Empty")
        item = self.array[1]
        self.array[1] = self.array[self.num_items]
        self.array[self.num_items] = None
        index = 1
        while True:
            if (index * 2) + 1 < self.size():
                if self.array[(index * 2) + 1] != None:
                    if self.array[index * 2] > self.array[(index * 2) + 1]:
                        if self.array[index*2] < self.array[index]:
                            temp = self.array[index * 2]
                            self.array[index * 2] = self.array[index]
                            self.array[index] = temp
                            index = index * 2
                        elif self.array[(index*2) + 1] < self.array[index]:
                            temp = self.array[(index * 2) + 1]
                            self.array[(index * 2) + 1]  = self.array[index]
                            self.array[index] = temp
                            index = index * 2
                        else:
                            break
            if index * 2 < self.size():
                if self.array[index*2] != None:
                    if self.array[index * 2] < self.array[index]:
                        temp = self.array[index * 2]
                        self.array[index * 2] = self.array[index]
                        self.array[index] = temp
                        index = index * 2
                    else:
                        break
                else:
                    break
            else:
                break
        self.num_items -= 1
        return item









