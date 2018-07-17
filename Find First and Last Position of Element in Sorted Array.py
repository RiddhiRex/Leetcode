class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(nums)-1
        if(len(nums)==0):
            return [-1, -1]
        elif(len(nums)==1):
            if(nums[0]==target):
                return [0, 0]
            else:
                return [-1, -1]

        mid = (l+r)//2
        while(l<=r):
            mid = (l+r)//2
            if(nums[mid]==target):
                l = mid
                r= mid
                while(l>=0 and nums[l]==target):
                    l=l-1
                while(r<len(nums) and nums[r]==target):
                    r=r+1
                return [l+1, r-1]
            elif(nums[mid]>target):
                r = mid-1
            elif(nums[mid]<target):
                l = mid+1

        return [-1, -1]
