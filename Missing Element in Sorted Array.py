class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        missing = [None]*len(nums)
        missing[0]=0
        for i in range(1, len(nums)):
            missing[i]=nums[i]-nums[i-1]-1+missing[i-1]
        print(missing)
        if k>missing[-1]:
            return nums[-1]+k-missing[-1]
        
        l=0
        r=len(nums)-1
        while(l!=r):
            mid = (l+r)//2
            if missing[mid]<k:
                l = mid+1
            else:
                r=mid
        print(l)
        return nums[l-1]+k-missing[l-1]
            
        
        
            
            
            
