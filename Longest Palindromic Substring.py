class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxlen=0
        st = ""
        l=0
        r=0
        if(len(s)<=1):
            return s
        for i in range(len(s)):
            for j in range(i+1, len(s)a+1):
                tmpst = s[i:j]
                if(tmpst == tmpst[::-1] and maxlen < len(tmpst)):
                    l =i
                    r=j
                    maxlen = len(tmpst)    
        return s[l:r]
                    
