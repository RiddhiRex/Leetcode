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
