class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if(needle not in haystack):
            return -1
        l=len(needle)
        for i in range(len(haystack)-l+1):
            print(haystack[i:i+l])
            if haystack[i:i+l]==needle:
                return i
        return 0
        
