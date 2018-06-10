class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target <nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        for each in nums:
            if each>=target:
                return nums.index(each)
