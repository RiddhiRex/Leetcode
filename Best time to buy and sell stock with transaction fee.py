class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        hold= -prices[0]
        cash=0
        for i in range(1, len(prices)):
            cash=max(cash, hold+prices[i]-fee)
            hold=max(hold, cash-prices[i])
        return cash
      
