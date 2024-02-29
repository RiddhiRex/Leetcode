class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))

        
        
        
solution 2
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if(s.isspace()):
            return s.strip()
        if(len(s)==0):
            return s
        words = s.split()
        res = " ".join(words[::-1])
        return res.strip()
            
