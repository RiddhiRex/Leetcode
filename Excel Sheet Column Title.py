class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans=""
        no=n
        while(no):
            ans=ans+chr((no-1)%26+ord("A"))
            no=(no-1)//26
        return ans[::-1]
            
            
        
