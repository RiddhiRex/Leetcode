class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(len(s)<=1):
            return len(s)
        tempstr = []
        maxlen=0
        for i in range(len(s)):
            if s[i] not in tempstr:
                tempstr.append(s[i])
                if(len(tempstr) > maxlen):
                    maxlen = len(tempstr)
            else:
                tempstr = tempstr[tempstr.index(s[i])+1:]
                tempstr.append(s[i])
        return maxlen
