#Based on the logic described here:https://www.youtube.com/watch?time_continue=1&v=jaNZ83Q3QGc
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        combination = [0]*(amount+1)
        combination[0]=1
        for coin in coins:
            for i in range(len(combination)):
                if i>=coin:
                    combination[i]+=combination[i-coin]
        return combination[amount]
            
        
