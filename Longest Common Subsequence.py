class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        
        # Initialize a DP table with dimensions (m+1) x (n+1)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        print(dp)
        
        # Iterate through the characters of text1 and text2
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    # If the characters match, extend the LCS by 1
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    # If the characters don't match, take the maximum LCS without including either character
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # The value at dp[m][n] will be the length of the longest common subsequence
        return dp[m][n]
