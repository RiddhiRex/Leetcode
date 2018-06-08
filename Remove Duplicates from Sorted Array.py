class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)<1):
            return 0
        j=1
        for i in range(1, len(nums)):
            if nums[i-1]!=nums[i]:
                if(nums[j]!=nums[i] or i==j):
                    nums[j]=nums[i]
                    j=j+1
        return j
