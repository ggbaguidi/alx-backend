#!/usr/bin/env python3
""" Task 3: module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO Caching
    """
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an key/item in the cache"""
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            newest_key = self.order.pop(-2)
            del self.cache_data[newest_key]
            print(f"DISCARD: {newest_key}")

    def get(self, key):
        """Get an item by key"""
        if key is None:
            return

        return self.cache_data.get(key)
