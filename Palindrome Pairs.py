import collections
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                w = words[i]+words[j]
                if w==w[::-1]:
                    ans.append([i, j])
                w=words[j]+words[i]
                if w==w[::-1]:
                    ans.append([j, i])
        return ans

import collections
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        ans = []
        dic={}
        for i, w in enumerate(words):
            dic[w]=i
        for i in range(len(words)):
            for j in range(len(words[i])+1):
                w1=words[i][j:]
                w2=words[i][:j]
                if w1==w1[::-1] and w2[::-1] in dic and dic[w2[::-1]]!=i:
                           ans.append([i, dic[w2[::-1]]])
                if j>0 and w2==w2[::-1] and w1[::-1] in dic and dic[w1[::-1]]!=i:
                           ans.append([dic[w1[::-1]], i])
        return ans
