#Based on the logic from https://www.youtube.com/watch?v=oDhu5uGq_ic

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        profit = [[0 for i in range(len(prices))] for j in range(k+1)]

        for i in range(1, k+1):
            for j in range(1, len(prices)):
                maxprofit = 0
                for m in range(0, j):
                    maxprofit = max(maxprofit, prices[j]-prices[m] + profit[i-1][m])
                profit[i][j]=max(profit[i][j-1], maxprofit)

        maxprofit = 0
        for i in range(k+1):
            maxprofit = max(maxprofit, profit[i][len(prices)-1])
        return maxprofit
        
        
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1 or k==0:
            return 0
        
        n=len(prices)
        profit= [[0 for x in range(n)] for y in range(k+1)]

        for i in range(1, k+1):
            for j in range(1, n):
                maxval=0
                for b in range(0, j):
                    maxval=max(maxval, (prices[j]-prices[b]+profit[i-1][b]))
                profit[i][j] = max(maxval,profit[i][j-1])
        maxprofit=0
        print(profit)
        for i in range(1, k+1):
            maxprofit=max(maxprofit, profit[i][n-1])
        return maxprofit
