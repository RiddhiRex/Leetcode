class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if(len(nums)<=1):
            return nums
        for i in range(1, len(nums)+1):
            if i in nums:
                while i in nums:
                    nums.remove(i)
            else:
                nums.append(i)
        return nums
