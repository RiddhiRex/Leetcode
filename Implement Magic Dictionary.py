class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mdict = []
        

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        
        self.mdict.extend(dict)
        return None
        

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for each in self.mdict:
            if len(each)==len(word):
                cnt=0
                print(word, each)
                for a, b in zip(word, each):
                    if a!=b:
                        cnt =cnt+1
                        if(cnt>1):
                            break
                if(cnt==1):
                    return True
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
