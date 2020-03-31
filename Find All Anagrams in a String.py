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
            
        
Solution 2:
    class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        pp = sorted(p)
        for i in range(len(s)-len(p)+1):
            if sorted(s[i:i+len(p)])==pp:
                ans.append(i)
        return ans
            
        
