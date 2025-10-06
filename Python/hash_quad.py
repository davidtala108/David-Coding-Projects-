import math
class HashTable:

    def __init__(self, table_size): # add appropriate attributes, NO default size
        ''' Initializes an empty hash table with a size that is the smallest
            prime number that is >= table_size (i.e. if 10 is passed, 11 will
            be used, if 11 is passed, 11 will be used.)'''
        if self.isPrime(table_size):
            self.table_size = table_size
        else:
            self.table_size = self.next_prime(table_size)
        self.key = [None] * self.table_size
        self.value = [None] * self.table_size
        self.num_items = 0

    def insert(self, key, value=None):
        ''' Inserts an entry into the hash table (using Horner hash function to determine index,
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value can be anything (Object, None, list, etc.).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is in the table, the new value replaces the existing value.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased
        to the next prime greater than 2*table_size.'''
        index = self.horner_hash(key) % self.table_size
        if self.key[index] != None:
            while self.key[index] != None:
                if self.key[index] == key:
                    self.value[index] = value
                    break
                index = self.collision_resolution(index,key)
            self.key[index] = key
            self.value[index] = value
        self.key[index]= key
        self.value[index]= value
        self.num_items += 1
        if self.get_load_factor() > 0.5:
            self.rehash()
    def collision_resolution(self,index,key):
        for i in range(self.table_size):
            Quad_Prob = (index + i ** 2) % self.table_size
            if self.key[Quad_Prob] == None or self.key[Quad_Prob] == key:
                    return Quad_Prob

    def rehash(self):
                old_key = self.key
                old_value = self.value
                old_size = self.table_size
                new_size = self.next_prime(2 * old_size)
                self.table_size = new_size
                self.key = [None] * new_size
                self.value = [None] * new_size
                self.num_items = 0
                for i in range(old_size):
                    if old_key[i] is not None:
                        self.insert(old_key[i], old_value[i])
    def horner_hash(self, key):
        ''' Compute the hash value by using Horner’s rule, as described in project specification.
            This method should not mod with the table size'''
        n = min(8,len(key))
        horner_hash = 0
        for i in range (n):
            horner_hash = horner_hash + ord(key[i])*31**(n-1-i)
        return horner_hash
    def next_prime(self, N):
        ''' Find the next prime number that is > n.'''
        if (N <= 1):
            return 2
        prime = N
        found = False
        while (not found):
            prime = prime + 1
            if (self.isPrime(prime) == True):
                found = True
        return prime
    def isPrime(self,n):
        if (n <= 1):
            return False
        if (n <= 3):
            return True
        if (n % 2 == 0 or n % 3 == 0):
            return False
        for i in range(5, int(math.sqrt(n) + 1), 6):
            if (n % i == 0 or n % (i + 2) == 0):
                return False
        return True
    def in_table(self, key):
        ''' Returns True if key is in an entry of the hash table, False otherwise.'''
        index = self.horner_hash(key) % self.table_size
        while self.key[index] != None:
                if self.key[index] == key:
                    return True
                index = self.collision_resolution(index, key)
        return False
    def get_index(self, key):
        ''' Returns the index of the hash table entry containing the provided key.
        If there is not an entry with the provided key, returns None.'''
        index = self.horner_hash(key) % self.table_size
        while self.key[index] != None:
                if self.key[index] == key:
                    return index
                index = self.collision_resolution(index, key)
        return None
    def get_all_keys(self):
        ''' Returns a Python list of all keys in the hash table.'''
        all_keys = []
        for val in self.key:
            if val != None:
                all_keys.append(val)
        return all_keys
    def get_value(self, key):
        ''' Returns the value associated with the key.
        If key is not in hash table, returns None.'''
        index = self.horner_hash(key) % self.table_size
        while self.key[index] != None:
            if self.key[index] == key:
                return self.value[index]
            index = self.collision_resolution(index, key)
        return None
    def get_num_items(self):
        ''' Returns the number of entries in the table.'''
        return self.num_items
    def get_table_size(self):
        ''' Returns the size of the hash table.'''
        return self.table_size

    def get_load_factor(self):
        ''' Returns the load factor of the hash table (entries / table_size).'''
        return (self.get_num_items()/self.get_table_size())