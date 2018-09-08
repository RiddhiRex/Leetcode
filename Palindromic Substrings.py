import itertools

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=[]
        cnt=0
        for i in range(0, len(s)):
            for j in range(i+1, len(s)+1):
                tmp = s[i:j]
                if tmp==tmp[::-1]:
                    cnt+=1
        return cnt
            
            
            
        
