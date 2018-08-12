class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i=1
        while(i<n):
            i=i*3
        if(i==n):
            return True
        else:
            return False
