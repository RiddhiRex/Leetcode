class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def getfirstidx(nums, target):
            l=0
            r=len(nums)-1
            while(l<=r):
                mid=l+(r-l)//2
                if(nums[mid]<target):
                    l=mid+1
                else:
                    r=mid-1
            return l
        
        def getlastidx(nums, target):
            l=0
            r=len(nums)-1
            while(l<=r): 
                mid=l+(r-l)//2
                if(nums[mid]<=target):
                    l=mid+1
                else:
                    r=mid-1
            return r

        first = getfirstidx(nums, target)
        last = getlastidx(nums, target)
        print(first, last)
        if(first<=last):
            return [first, last]
        else:
            return [-1, -1]
                
        
