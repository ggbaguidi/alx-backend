#!/usr/bin/env python3
""" Task 1: module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching
    """
    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """put new key/item into the cache"""

        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = self.order.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """retrieve item for cache by using key"""
        if key is None:
            return

        return self.cache_data.get(key)
