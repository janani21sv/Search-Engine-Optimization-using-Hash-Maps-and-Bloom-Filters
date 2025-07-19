import sys
print(sys.path)


import math
from bitarray import bitarray


class BloomFilter:
    def __init__(self, capacity, false_positive_rate):
        self.capacity = capacity
        self.false_positive_rate = false_positive_rate
        self.size = self.calculate_size()
        self.num_hash_functions = self.calculate_num_hash_functions()
        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)

    def add(self, item):
        for seed in range(self.num_hash_functions):
            hash_val = self.hash(item, seed)
            self.bit_array[hash_val] = 1

    def exists(self, item):
        for seed in range(self.num_hash_functions):
            hash_val = self.hash(item, seed)
            if not self.bit_array[hash_val]:
                return False
        return True

    def calculate_size(self):
        size = -self.capacity * math.log(self.false_positive_rate) / (math.log(2) ** 2)
        return int(size)

    def calculate_num_hash_functions(self):
        num_hash_functions = (self.size / self.capacity) * math.log(2)
        return int(num_hash_functions)

    def hash(self, item, seed):
        return hash(item + str(seed)) % self.size
