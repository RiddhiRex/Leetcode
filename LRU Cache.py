class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.lru=collections.OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.lru:
            val = self.lru[key]
            self.lru.pop(key)
            self.lru[key]=val
            return val
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.lru:
            self.lru.pop(key)
        else:
            if (len(self.lru)==self.capacity):
                self.lru.popitem(last=False)
        self.lru[key]=value
        return
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
