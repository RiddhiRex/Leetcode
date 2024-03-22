class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])

        return dp[-1]
        
        
        
class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.insert(0, 0)
        nums.insert(0, 0)
        ans = [0 for _ in range(len(nums))]
        for i in range(2, len(nums)):
            ans[i]=max(ans[i-2]+nums[i], ans[i-1])
        return ans[-1]
        
