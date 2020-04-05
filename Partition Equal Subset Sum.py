'''
Given a non-empty array containing only positive integers, 
find if the array can be partitioned into two subsets such 
that the sum of elements in both subsets is equal.

Note: dp = [False] * (sum//2)+1
make dp[i]=1 if dp[i] or dp[num-i] where num in nums and 1<=i<=len(dp)

'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2!=0:
            return False
        dp = [False] * (total//2 + 1)
        dp[0]=True
        for n in nums:
            for i in reversed(range(1,len(dp))):
                if i>=n:
                    dp[i]=dp[i] or dp[i-n]
        return dp[-1]
        
