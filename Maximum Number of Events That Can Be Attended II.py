class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events = sorted(events, key =operator.itemgetter(1))
        sorted_ends = [x[1] for x in events]
        dp = [[0]*(k+1) for _ in range(len(events)+1)]
        print(dp)
        for i in range(1, len(events)+1):
            prev_i_m_1 = bisect.bisect_left(sorted_ends, events[i-1][0])
            print(i, prev_i_m_1, events[i-1][0], sorted_ends)
            for j in range(1, k+1):
                dp[i][j] = max(dp[i-1][j], dp[prev_i_m_1][j-1]+events[i-1][2])
        return dp[-1][-1]
