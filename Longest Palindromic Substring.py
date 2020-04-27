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
            for j in range(i+1, len(s)):
                tmpst = s[i:j]
                if(tmpst == tmpst[::-1] and maxlen < len(tmpst)):
                    l =i
                    r=j
                    maxlen = len(tmpst)    
        return s[l:r]

    #Solution 2
    class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_from_center(s, l , r):
            while(l>=0 and r<len(s) and s[l]==s[r]):
                l-=1
                r+=1
            return r-l-1
        
        if len(s)==0 or len(s)==1:
            return s
        st = 0
        end = 0
        for i in range(len(s)):
            l1 = expand_from_center(s, i, i)
            l2 = expand_from_center(s, i, i+1)
            l = max(l1, l2)
            if l>end-st:
                st = i-(l-1)//2
                end = i+l//2
            print(st, end, l)
                
        return s[st:end+1]
    
                
