class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if(len(prices)==0):
            return 0
        minp = prices[0]
        maxprofit=0
        for i in range(len(prices)):
            if(prices[i]<minp):
                minp=prices[i]
            
            elif(prices[i]-minp>maxprofit):
                maxprofit = prices[i]-minp
        return maxprofit
