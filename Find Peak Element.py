class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if(len(nums)<3):
            n = max(nums)
            return nums.index(n)
        for i in range(0, len(nums)):
            if(i==0 and nums[i]>nums[i+1]):
                return i
            elif(i==len(nums)-1 and nums[i]>nums[i-1]):
                return i
            elif(nums[i]>nums[i-1] and nums[i]>nums[i+1]):
                return i
        
