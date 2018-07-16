class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def longstr(s, k, start, end):
            maxlen=0
            count = {}
            i = start
            for each in s[start:end]:
                if ord(each)-ord('a') not in count.keys():
                    count[ord(each)-ord('a')]=1
                else:
                    count[ord(each)-ord('a')]+=1
            while(i<end):
                while(i<end and count[ord(s[i])-ord('a')] < k):
                    i=i+1
                j = i
                while(j<end and count[ord(s[j])-ord('a')]>=k):
                    j=j+1
                if(i==start and j==end):
                    return end-start
                maxlen = max(maxlen , longstr(s, k, i, j))
                i = j
            return maxlen
        return longstr(s, k, 0, len(s))
