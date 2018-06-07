class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        no=1
        c=0
        for i in range(1, n+1):
            no=no*i
        while(no%10==0):
            c=c+1
            no=no//10
        return c
