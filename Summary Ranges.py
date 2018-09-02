class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        nums=sorted(nums)
        ans=[]
        i=0
        while(i<len(nums)):
            x = nums[i]
            if(i<len(nums)-1 and nums[i]+1==nums[i+1]):
                while(i<len(nums)-1 and nums[i+1]==(nums[i]+1)):
                    i=i+1
                ans.append(str(x)+"->"+str(nums[i]))
            else:
                ans.append(str(x))
            i=i+1
        return ans
            
            
            
