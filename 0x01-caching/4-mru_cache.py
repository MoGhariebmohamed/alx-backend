#!/usr/bin/env python3
"""
this is base model
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
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
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                most_recent_use, any = self.cache_data.popitem(False)
                print("DISCARD:", most_recent_use)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        to get the cash content
        """
        if not key:
            return None
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
