class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = collections.Counter(words)
        ans = []
        heap = []
        for key, val in dic.items():
            heap.append([-val, key])
        heapq.heapify(heap)
        while(k>0):
            ans.append(heapq.heappop(heap)[1])
            k-=1
        return ans


        
        
        
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = collections.Counter(words)
        ans = []
        result = sorted(dic.items(), key=lambda item: (-item[1], item[0])) 
        print(result)
        ans = [each[0] for each in result]
        return ans[:k]
        
        
        
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
        
Solution 2(not definite):
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wrds = collections.Counter(words)
        ans = []
        wds = sorted(wrds.items(), key=operator.itemgetter(1), reverse=True)[:k]
        for i, w in enumerate(wds):
                ans.append(w[0])
        return ans
            
        
