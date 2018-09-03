#solution1:
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        for i in range(len(s)-9):
            if i==0:
                if s[i:10] in s[i+1:len(s)]:
                    ans.append(s[i:10])
            else:
                if s[i:i+10] in s[i+1:len(s)] or s[i:i+10] in s[0:i+9]:
                    if s[i:i+10] not in ans:
                        ans.append(s[i:i+10])
        return ans
        
#solution 2:
import collections
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l = []
        ans=[]
        for i in range(len(s)-9):
            l.append(s[i:i+10])
        for k, v in collections.Counter(l).items():
            if v>1:
                ans.append(k)
        return ans

