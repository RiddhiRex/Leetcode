class Solution:
    def reverse(self, s, start, end):
        while(start<end):
            t=s[start]
            s[start], s[end]=s[end], t
            start=start+1
            end=end-1
        
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        idx=0
        for i in range(len(str)):
            if str[i]==" ":
                self.reverse(str, idx, i-1)
                idx=i+1        
        self.reverse(str, idx, len(str)-1)
        str.reverse()
        
        
        
