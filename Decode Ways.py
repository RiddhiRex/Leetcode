#dp[i]  =   dp[i−1]+dp[i−2],   10 <=s[i-2:2]<=26 and s[i−2:2]!=[10 or 20]
#           dp[i−2],   s[i-2:i] = [10 or 20]
#           dp[i−1],   others

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp=[0]*(len(s)+1)
        dp[0]=1
        dp[1]=1
        if len(s)==0 or s[0]=="0":
            return 0
        for i in range(2, len(s)+1):
            if 10<= int(s[i-2:i])<=26 and s[i-1]!="0":
                dp[i]=dp[i-2]+dp[i-1]
                
            elif int(s[i-2:i])==20 or int(s[i-2:i])==10:
                dp[i]=dp[i-2]
                
            elif s[i-1]!="0":
                dp[i]=dp[i-1]
                
            else:
                return 0
        return dp[len(s)]

        
        
                
                
        
