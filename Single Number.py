class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for no in nums:
            ans ^=no
        return ans
            
