# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        m=1
        if(guess(n)>1):
            return 0
        elif(guess(n)==0):
            return n
        while(m<=n):
            if(guess((m+n)//2)==-1):
                n=(m+n)//2
            elif(guess((m+n)//2)==1):
                m=(m+n)//2
            elif(guess((m+n)//2)==0):
                return ((m+n)//2)
        return 0
