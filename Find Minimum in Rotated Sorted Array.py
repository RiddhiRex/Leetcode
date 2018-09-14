class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start=0
        end=len(nums)-1
        while(start<end and nums[start]>=nums[end]):
            mid=(start+end)//2
            if(nums[mid]<nums[start]):
                end=mid
            else:
                start=mid+1
        return nums[start]
            
            
