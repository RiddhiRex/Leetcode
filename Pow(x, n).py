#logic from https://www.youtube.com/watch?v=wAyrtLAeWvI
#time complexity = O(log n)
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        elif n==1:
            return x
        if(x==0 or x==1):
            return x
        if(n%2==0):
            y=self.myPow(x, abs(n)/2)
            if(n>0):
                return y*y
            else:
                return 1/(y*y)
        else:
            
            y = x*self.myPow(x, abs(n)-1)
            if n<0:
                return 1/y
            else:
                return y
            

        
