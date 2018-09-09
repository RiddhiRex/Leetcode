class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if(numerator%denominator==0):
            return str(numerator/denominator)
        res=""
        if(numerator<0 and denominator>0 or numerator>0 and denominator<0):
            res+="-"
        num = abs(numerator)
        den= abs(denominator)
        res +=str(num/den)
        num=num%den
        
        if(num>0):
            res+="."
        lookup = {}
        while(num and num not in lookup):
            lookup[num]=len(res)
            num=num*10
            res+=str(num/den)
            num=num%den
            
        if num in lookup:
            return res[:lookup[num]]+"("+ res[lookup[num]:] +")"
        return res
            
                
        
        
        
