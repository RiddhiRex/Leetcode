class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = []
        for each in range(len(nums)+1):
                l.extend(list(itertools.combinations(nums, each)))
        return l
        
