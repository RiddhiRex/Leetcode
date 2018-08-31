class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = bin(n)
        n = str(n)
        cnt=0
        for each in n:
            if each=="1":
                cnt=cnt+1
        return cnt
        
