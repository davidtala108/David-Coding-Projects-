
#SEPREATING CHAIN
class KeyNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashTable:

    def __init__(self, table_size = 11):
        self.table_size = table_size
        self.hash = [None] * self.table_size
        self.num_items = 0
        self.num_collisions = 0


    def insert(self, key, item = None):
        N = KeyNode(key,item)
        try:
            index = key % self.table_size
        except:
            new_key = 0
            for val in key:
                new_key +=ord(val)
            index = new_key % self.table_size
        if self.hash[index] == None or self.hash[index].key == key:
            self.hash[index] = N
        else:
            self.num_collisions += 1
            self.hash[index].next = N
        self.num_items += 1

        if self.load_factor()> 1.5:
            self.table_size = (self.table_size * 2) + 1
            old_hash = self.hash
            self.hash = [None] * self.table_size
            self.rehash(old_hash)
    def rehash(self,old):
            for i in range(len(old)):
                if old[i] != None:
                    self.insert(old[i].key,old[i].value)
                    while True:
                        if old[i].next != None:
                            old[i] = old[i].next
                            self.insert(old[i].key, old[i].value)
                        else:
                            break

    def get(self,key):
        try:
            index = key % self.table_size
        except:
            new_key = 0
            for val in key:
                new_key += ord(val)
            index = new_key % self.table_size

        if self.hash[index] == None:
            raise LookupError
        else:
            get = self.hash[index]
            while True:
                if get.key != key:
                    get = get.next
                    if get == None:
                        raise LookupError
                else:
                    break
            return (get.key, get.value)
    def remove(self,key):
        try:
            index = key % self.table_size
        except:
            new_key = 0
            for val in key:
                new_key += ord(val)
            index = new_key % self.table_size
        if self.hash[index] == None:
            return LookupError
        else:
            remove = self.hash[index]
            prev = None
            while True:
                if remove.key != key:
                    prev = remove
                    remove = remove.next
                    if remove == None:
                        raise LookupError
                else:
                    break
            items = (remove.key, remove.value)
            if prev != None:
                prev.next = remove.next
            else:
                self.hash[index] = remove.next
            self.num_items -= 1
            return items
    def size(self):
        return self.num_items
    def load_factor(self):
        return self.num_items / self.table_size

    def collisions(self):
        return self.num_collisions
    def size2(self):
        return self.table_size

