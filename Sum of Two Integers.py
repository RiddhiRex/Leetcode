class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if(a==0):
            return b
        if(b==0):
            return a

        while(b!=0):
            c=a&b
            a =a^b
            b=c<<1
        return a
