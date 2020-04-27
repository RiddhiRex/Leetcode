class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = []
        ans = []
        for i in range(len(nums)):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            if dq[0] == i-k:
                dq.pop(0)
            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans
        
