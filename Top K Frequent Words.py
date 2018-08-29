class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        wdict = {}
        for each in sorted(words):
            if each not in wdict:
                wdict[each]=1
            else:
                wdict[each]+=1
        return sorted(sorted(wdict), key=wdict.get, reverse=True)[:k]
        
