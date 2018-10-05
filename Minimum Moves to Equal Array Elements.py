class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums))<=1:
            return 0
        ans = sum(nums)-min(nums)*len(nums)
        return ans
