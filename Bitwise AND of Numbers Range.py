class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ans = m
        for each in range(m+1, n+1):
            ans = ans & each
        return (ans)
