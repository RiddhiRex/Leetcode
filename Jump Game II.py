class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        jumps = 0
        current_max_reach = 0 #the maximum reachable position with the current number of jumps (current_max_reach)
        farthest = 0 #farthest position that can be reached from the current position (farthest) 
        
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_max_reach:
                jumps += 1
                current_max_reach = farthest
                if current_max_reach >= n - 1:
                    break
        return jumps

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
                
