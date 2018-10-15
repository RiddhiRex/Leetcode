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

    #method 2
# can use a set and dictionary or can use dictionary with collections.Counter and get the first element in array with count 1
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        unique = set()
        d = collections.defaultdict(int)
        for i, c in enumerate(s):
            if c in d:
                if d[c] in unique:
                    unique.remove(d[c])
            else:
                unique.add(i)
                d[c]=i
        if unique:
            return min(unique)
        else:
            return -1
