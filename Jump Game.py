class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        step = nums[0]
        if(len(nums)<=1):
            return True
        for i in range(1, len(nums)):
            if step>0:
                step-=1
                step=max(step, nums[i])
            else:
                return False 
        return True
