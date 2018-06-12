class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            if(i==0):
                if(s[i] not in s[i+1:]):
                    return i
            elif(s[i] not in s[0:i] and s[i] not in s[i+1:]):
                return i
        return -1
