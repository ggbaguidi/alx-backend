#!/usr/bin/env python3
""" Task 0: module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Basic dictionary
    """
    def put(self, key, item):
        """put new key/item into the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """retrieve item for cache by using key"""
        if key is None:
            return

        return self.cache_data.get(key)
