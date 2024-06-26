#!/usr/bin/env python3
"""
this is pagination function
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    cashing system inherted from base class
    """

    def put(self, key, item):
        """
        to add cash items
        """
        if not key or item:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        to get the cash content
        """
        if not key:
            return
        return self.cache_data.get(key, None)

my_cache = BasicCache()
my_cache.print_cache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
print(my_cache.get("D"))
my_cache.print_cache()
my_cache.put("D", "School")
my_cache.put("E", "Battery")
my_cache.put("A", "Street")
my_cache.print_cache()
print(my_cache.get("A"))