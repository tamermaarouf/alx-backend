#!/usr/bin/env python3
'''
a class BasicCache that inherits from BaseCaching
'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''BasicCache that inherits from BaseCaching and is a caching system:
    You must use self.cache_data - dictionary from the parent class BaseCaching
    This caching system doesn’t have limit
    '''
    def __init__(self):
        '''Initiliaze
        '''
        super().__init__()

    def put(self, key, item):
        '''Must assign to the dictionary
        self.cache_data the item value for the key key.
        If key or item is None, this method should not do anything.
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        '''
        return self.cache_data.get(key, None)
