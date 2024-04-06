class LFUCache:

    def __init__(self, capacity: int):
        cache = collections.defaultdict(int)
        self.capacity = capacity
        self.currcnt = 0
        self.freq_to_keys = collections.defaultdict(OrderedDict)
        self.key_to_valfreq = {}
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key in self.key_to_valfreq:
            val, freq = self.key_to_valfreq[key]
            del self.freq_to_keys[freq][key]
            if not self.freq_to_keys[freq]:
                del self.freq_to_keys[freq]
                if freq == self.min_freq:
                    self.min_freq += 1
            self.freq_to_keys[freq + 1][key] = None
            self.key_to_valfreq[key] = [val, freq + 1]
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_valfreq:
            self.get(key)  #Update frequency
            self.key_to_valfreq[key][0] = value  #Update value
        else:
            if len(self.key_to_valfreq) >= self.capacity:
                del_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
                del self.key_to_valfreq[del_key]
            self.key_to_valfreq[key] = [value, 1]
            self.freq_to_keys[1][key] = None
            self.min_freq = 1
            


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
