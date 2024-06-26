#!/usr/bin/env python3
"""
this is base model
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    cashing system inherted from base class
    """

    def __init__(self):
        """
        init function
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        to add cash items
        """
        if not key or not item:
            return
        if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
            least_recent_use, any = self.cache_data.popitem(True)
            print("DISCARD:", least_recent_use)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """
        to get the cash content
        """
        if not key:
            return None
        return self.cache_data.get(key, None)
my_cache = LRUCache()
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
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()