class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        def findSum(i, cur_sum, target):
            if i==len(nums) and cur_sum==target:
                self.cnt+=1
            elif i<len(nums):
                findSum(i+1, cur_sum+nums[i], target)
                findSum(i+1, cur_sum-nums[i], target)
                
        self.cnt = 0
        findSum(0, 0, S)
        return self.cnt
        
