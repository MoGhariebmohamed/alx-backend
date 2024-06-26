#!/usr/bin/env python3
"""
this is base model
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
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
            last_key, any = self.cache_data.popitem(True)
            print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """
        to get the cash content
        """
        if not key:
            return None
        return self.cache_data.get(key, None)
