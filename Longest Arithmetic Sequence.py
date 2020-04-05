class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = collections.defaultdict(int)
        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
                v =  A[j]-A[i]
                dp[v, j] = max(dp[v, j], dp[v, i]+1)
        return max(dp.values())+1
