class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        c=0
        a = bin(x)[2:]
        b = bin(y)[2:]
        r=0
        if(len(a)>len(b)):
            d = len(a)-len(b)
            for i in range(d):
                b= '0'+b
        elif(len(b)>len(a)):
            d = len(b)-len(a)
            for i in range(d):
                a= '0'+a
        for i in range(len(a)):
            if(a[i]!=b[i]):
                r=r+1        
        #c=a^b
        #while(c>0):
        #   r=r+c&1
        #  c=c>>1
        return r
