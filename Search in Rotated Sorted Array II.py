class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
    
        l=0
        r=len(nums)-1
        while(l<=r):
            #mid=(l+r)//2
            mid = l+(r-l)//2

            if(nums[mid]==target):
                return True
            if nums[l]==nums[mid]==nums[r]:
                r-=1
                l+=1
            elif nums[mid]>target:
                if nums[l]<=target or nums[mid]<nums[l]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if nums[l]>target or nums[mid]>=nums[l]:
                    l=mid+1
                else:
                    r=mid-1

        return False
            
