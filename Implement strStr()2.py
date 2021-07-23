         class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if(len(haystack)==len(needle) and haystack==needle):
            return 0
        for n in range(0, len(haystack)-len(needle)+1):
            if haystack[n:n+len(needle)]==needle:
                return n
        return -1
        
        
        Submission 2:
        class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1

    
