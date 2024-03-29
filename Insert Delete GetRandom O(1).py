class RandomizedSet:

    def __init__(self):
        self.d = {}
        self.l = []

    def insert(self, val: int) -> bool:
        if val not in self.d:
            self.d[val]=len(self.l)
            self.l.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if len(self.l)==0:
            return False
        if val in self.d:
            idx = self.d.pop(val)
            if idx!=len(self.l)-1:
                last_elemt = self.l.pop()
                self.l[idx]=last_elemt
                self.d[last_elemt] = idx
            else:
                self.l.pop()
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return random.choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


solution 2:
class RandomizedSet:

    def __init__(self):
        self.d = {}

    def insert(self, val: int) -> bool:
        if val not in self.d:
            self.d[val]=1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.d:
            self.d.pop(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return random.choice(list(self.d.keys()))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()





solution 2:
import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.l = []
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.l:
            self.dic[val]=1
            self.l.append(val)
            return True
        else:
            return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.l:
            return False
        else:
            self.dic.pop(val)
            self.l.remove(val)
            return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        l = self.l
        n = random.sample(l, 1)
        return n[0]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
