#!/usr/bin/env python3
'''Create a class LIFOCache
'''
BasicCache = __import__('0-basic_cache').BasicCache


class LIFOCache(BasicCache):
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

    def put(self, key, item):
        '''Must assign to the dictionary self.cache_data
        the item value for the key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is
        higher that BaseCaching.MAX_ITEMS:
        you must discard the last item put in cache (LIFO algorithm)
        print DISCARD: with the key discarded and following by a new line
        '''

        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > self.MAX_ITEMS:
                last_key = list(self.cache_data)[-1]
                self.cache_data.pop(last_key)
                print(f'DISCARD: {last_key}')
            self.cache_data[key] = item
