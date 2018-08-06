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
        
        
