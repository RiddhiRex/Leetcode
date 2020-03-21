class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        if len(p)>len(s):
            return []
        l = list(p)
        d = collections.Counter(l)
        ans = []
        for i in range(len(s)):
            if collections.Counter(s[i:i+len(p)]) == d:
                ans.append(i)
        return ans
            
        
