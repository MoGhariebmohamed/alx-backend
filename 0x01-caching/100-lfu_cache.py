#!/usr/bin/env python3
"""
this is base model
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """
    cashing system inherted from base class
    """

    def __init__(self):
        """
        init function
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = []

    def repeat_funct(self, mru_key):
        """Reorders the items in this cache based on the most
        recently used item.
        """
        max_positions = []
        mru_freq = 0
        mru_pos = 0
        ins_pos = 0
        for i, key_freq in enumerate(self.keys_freq):
            if key_freq[0] == mru_key:
                mru_freq = key_freq[1] + 1
                mru_pos = i
                break
            elif len(max_positions) == 0:
                max_positions.append(i)
            elif key_freq[1] < self.keys_freq[max_positions[-1]][1]:
                max_positions.append(i)
        max_positions.reverse()
        for pos in max_positions:
            if self.keys_freq[pos][1] > mru_freq:
                break
            ins_pos = pos
        self.keys_freq.pop(mru_pos)
        self.keys_freq.insert(ins_pos, [mru_key, mru_freq])

    def put(self, key, item):
        """
        to add cash items
        """
        if not key or not item:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                less_freq_use, any = self.keys_freq[-1]
                self.cache_data.pop(less_freq_use)
                self.keys_freq.pop()
                print("DISCARD:", less_freq_use)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
            for x, keys_freq in enumerate(self.keys_freq):
                if keys_freq[1] == 0:
                    insert = x
                    break
                self.keys_freq.insert(insert, [key, 0])
        else:
            self.cache_data[key] = item
            self.repeat_funct(key)

    def get(self, key):
        """
        to get the cash content
        """
        if not key:
            return None
        if key is not None and key in self.cache_data:
            self.repeat_funct(key)
        return self.cache_data.get(key, None)

my_cache = LFUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
print(my_cache.get("I"))
print(my_cache.get("H"))
print(my_cache.get("I"))
print(my_cache.get("H"))
print(my_cache.get("I"))
print(my_cache.get("H"))
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()
my_cache.put("L", "L")
my_cache.print_cache()
my_cache.put("M", "M")
my_cache.print_cache()