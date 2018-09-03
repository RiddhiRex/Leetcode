import collections
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cnt=0
        st = collections.Counter(s)
        for v in st.values():
            if v%2!=0:
                cnt=cnt+1
            if cnt >1:
                return False

        return True

        
