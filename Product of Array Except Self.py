from numpy import prod
class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = []
        for i in range(len(nums)):
            m = itertools.combinations(nums[0:i]+nums[i+1:], len(nums)-1)
            out.append(prod(list(m)))
        return out
