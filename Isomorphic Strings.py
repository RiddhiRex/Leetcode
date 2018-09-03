class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapdict={}
        for a, b in zip(s, t):
            if(a not in mapdict.keys()):
                if b not in mapdict.values():
                    mapdict[a]=b
                else:
                    return False
            else:
                if b!=mapdict[a]:
                    return False
        return True
            
