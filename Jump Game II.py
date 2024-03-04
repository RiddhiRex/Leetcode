class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)<=1):
            return 0
        
        jumps = [float("inf")]*len(nums)
        jumps[0]=0
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j]+j>=i:
                    jumps[i]=min(jumps[i], jumps[j]+1)
        return jumps[len(nums)-1]
        


#As per the logic from https://www.youtube.com/watch?v=cETfFsSTGJI
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)<=1):
            return 0
        
        jumps = [float("inf")]*len(nums)
        jumps[0]=0
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j]+j>=i:
                    jumps[i]=min(jumps[i], jumps[j]+1)
        return jumps[len(nums)-1]
                
