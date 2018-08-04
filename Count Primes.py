class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n<2):
            return 0
        pno =[True]*n
        cnt = 0
        pno[0]=False
        pno[1]=False
        for each in range(2, int(n**0.5)+1):
            if(pno[each]==True):
                pno[each*each:n:each]=[False]*len(pno[each*each:n:each])

        return sum(pno)
    
