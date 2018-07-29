class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1 or n==0:
            return 1
        elif n==2:
            return 2
        else:
            cnt = 0
            for i in range(n):
                cnt+=(self.numTrees(i)*self.numTrees(n-i-1))
            return cnt
        
