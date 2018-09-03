class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign=1
        if((dividend<0)^(divisor<0)):
            sign=-1
        dividend = abs(dividend)
        divisor = abs(divisor)
        q=0
        while(dividend>=divisor):
            dividend=dividend-divisor
            q=q+1
        return sign*q
        
