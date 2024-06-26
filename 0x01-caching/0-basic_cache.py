#!/usr/bin/env python3
"""
this is base model
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
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        to get the cash content
        """
        if not key:
            return None
        return self.cache_data.get(key, None)
