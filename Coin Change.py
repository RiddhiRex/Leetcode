#You are given coins of different denominations and a total amount of money amount. 
#Write a function to compute the fewest number of coins that you need to make up that amount. 
#If that amount of money cannot be made up by any combination of the coins, return -1.

#Logic taken from https://www.youtube.com/watch?v=NJuKJ8sasGk

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        cnt = [float("inf")]*(amount+1)
        cnt[0]=0

        for coin in coins:
            for i in range(len(cnt)):
                if(i>=coin):
                    cnt[i]=min(cnt[i], cnt[i-coin]+1)
                    
        if(cnt[amount]==float("inf")):
            return -1
        else:
            return cnt[amount]
