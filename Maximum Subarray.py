class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float("-inf")
        total = 0
        
        for n in nums:
            total+=n
            if total > maxsum:
                maxsum = total
            if total<0:
                total=0
        return maxsum
        
solution 2
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)==0):
            return 0
        if(max(nums)<0):
            return max(nums)
        max_so_far=0
        highest =0
        for i in range(0, len(nums)):
            max_so_far+=nums[i]
            if max_so_far<0:
                max_so_far=0
            if(max_so_far>highest):
                highest=max_so_far
        return highest            
