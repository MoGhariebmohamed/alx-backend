#!/usr/bin/env python3
"""
this is base model
"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
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
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, any = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """
        to get the cash content
        """
        if not key:
            return None
        return self.cache_data.get(key, None)
