class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pt = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[pt]= nums[i]
                pt=pt+1
        for i in range(pt, len(nums)):
            nums[i]=0
            
