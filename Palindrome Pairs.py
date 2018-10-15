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
