#!/usr/bin/env pythn3
""" Task 4: module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRU Caching
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
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

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
