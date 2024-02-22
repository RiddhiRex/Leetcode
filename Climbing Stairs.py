class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev =0
        curr = 1
        for i in range(n):
            prev, curr = curr, prev+curr
        return curr

Solution 2:
def climb_stairs(n):
    if n <= 2:
        return n
    
    # Initialize a list to store the number of ways to reach each step
    dp = [0] * (n + 1)
    
    # Base cases
    dp[1] = 1
    dp[2] = 2
    
    # Dynamic programming approach to compute the number of ways
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


Solution 3: 
#     def climbStairs(self, n: int) -> int:
#         if n == 1:
#             return 1
#         if n == 2: 
#             return 2
#         if n >= 3:
#             return self.climbStairs(n-1)+self.climbStairs(n-2)
