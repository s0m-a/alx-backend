#!/usr/bin/env python3
"""Basic caching module.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Rep an object which  allows storing and
    retrieving items from a dictionary.
    """
    def put(self, key, item):
        """puts
        puts an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        gets an item by key.
        """
        return self.cache_data.get(key, None)
