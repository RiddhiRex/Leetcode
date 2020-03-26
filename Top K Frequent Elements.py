import operator
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dict= {}
        l = []
        for each in nums:
            if each not in dict.keys():
                dict[each]=1
            else:
                dict[each]=dict[each]+1
        for each in sorted(dict.items(), key=operator.itemgetter(1), reverse=True)[:k]:
            l.append(each[0])
        return l

    
    solution 2:
    class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = collections.Counter(nums)
        l = sorted(d.items(), key=operator.itemgetter(1), reverse=True)[0:k]
        return [i for i,j in l]
        
