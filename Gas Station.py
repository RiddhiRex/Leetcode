class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start_idx = 0
        total_sum = 0
        cur_sum = 0
        for i in range(len(gas)):
            dif = gas[i]-cost[i]
            cur_sum += dif
            total_sum += dif
            if cur_sum<0:
                start_idx = i+1
                cur_sum=0
        if total_sum>=0:
            return start_idx
        else:
            return -1
