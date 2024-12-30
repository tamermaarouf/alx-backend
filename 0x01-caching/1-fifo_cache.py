#!/usr/bin/env python3
'''Create a class FIFOCache
'''
BasicCache = __import__('0-basic_cache').BasicCache


class FIFOCache(BasicCache):
    '''that inherits from BaseCaching and is a caching system:
    You must use self.cache_data - dictionary from the parent class BaseCaching
    You can overload def __init__(self):
    but don’t forget to call the parent init: super().__init__()
    '''
    def __init__(self):
        '''Initiliaze
        '''
        super().__init__()


    def get(self, key):
        '''Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None.
        '''
        return self.cache_data.get(key, None)
