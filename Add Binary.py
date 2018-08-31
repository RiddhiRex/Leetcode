class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a= a[::-1]
        b = b[::-1]
        sum=0
        sol = []
        for i in range(max(len(a), len(b))):
            if(i<len(a) and a[i]=="1"):
                sum=sum+1
            if(i<len(b) and b[i]=="1"):
                sum=sum+1
            sol.insert(0, str(sum%2))
            sum=sum//2
        if(sum>0):
            sol.insert(0, str(sum%2))
        return "".join(sol)
        
            
            
        
