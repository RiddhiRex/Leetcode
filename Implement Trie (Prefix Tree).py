class TrieNode():
    def __init__(self):
        self.child = {}
        self.isLeaf=False
        
class Trie(object):
            
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.getNode()
        
    def getKey(self, ch):
        return ord(ch)-ord('a')

    def getNode(self):
        return TrieNode()
    
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for i in range(len(word)):
            key = self.getKey(word[i])
            if key not in node.child.keys():
                node.child[key]=self.getNode()
            node=node.child[key]
        node.isLeaf=True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if(len(word)==0):
            return False
        
        node = self.root
        for i in range(len(word)):
            key = self.getKey(word[i])
            if key not in node.child.keys():
                return False
            else:
                node=node.child[key]
        return node.isLeaf
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if(len(prefix)==0):
            return False
        node = self.root
        for i in range(len(prefix)):
            key = self.getKey(prefix[i])
            if key not in node.child.keys():
                return False
            else:
                node=node.child[key]
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
