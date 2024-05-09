#!/usr/bin/env python3
"""This a first-In First-Out caching module.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """This  an object which  allows storing and
    retrieving items from a dictionary with a FIFO
    removal mechanism.
    """
    def __init__(self):
        """This intialize  the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """gets an item by key.
        """
        return self.cache_data.get(key, None)
