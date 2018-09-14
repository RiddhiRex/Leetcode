class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        l=float("inf")
        low=0
        total=0
        for high in range(len(nums)):
            total+=nums[high]
            while(total>=s):
                l = min(l, high-low+1)
                total-=nums[low]
                low+=1
        
        if l==float("inf"):
            return 0
        else:
            return l
