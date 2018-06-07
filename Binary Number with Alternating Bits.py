class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        no = bin(n)[2:]
        print(no)
        i=1
        prev= no[0]
        while(i<len(no)):
            if(no[i]==prev):
                return (False)
            prev = no[i]
            i=i+1
        return (True)
        
