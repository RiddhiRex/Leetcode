class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = 0
        r=len(nums)-1
        mid = 0
        while(mid<=r):
            if(nums[mid]==0):
                tmp = nums[mid]
                nums[mid] = nums[l]
                nums[l] = tmp
                l=l+1
                mid=mid+1
            elif(nums[mid]==2):
                tmp = nums[mid]
                nums[mid] = nums[r]
                nums[r] = tmp
                r=r-1
            else:
                mid=mid+1
            print(nums)
        
                
                
