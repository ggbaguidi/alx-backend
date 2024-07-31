#!/usr/bin/env pythn3
""" Task 5: module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRU Caching
    """
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:

            # Update the item's position in the order list
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Evict the least recently used item
            mru_key = self.order.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        self.order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        # Update the item's position in the order list
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
