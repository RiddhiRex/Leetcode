class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        b = word.isupper()
        if(b==True):
            return True
        b = word.islower()
        if(b):
            return True
        b = word[0].isupper() and word[1:].islower()
        if(b):
            return True
        return False
        
