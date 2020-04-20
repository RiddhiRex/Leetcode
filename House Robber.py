class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.insert(0, 0)
        nums.insert(0, 0)
        ans = [0 for _ in range(len(nums))]
        for i in range(2, len(nums)):
            ans[i]=max(ans[i-2]+nums[i], ans[i-1])
        return ans[-1]
        
