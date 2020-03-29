class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        ans = 0
        total = 0
        max_unsat = 0
        for i in range(len(customers)):
            if grumpy[i]==0:
                ans += customers[i]
            else:
                total+=customers[i]
            if i>=X:
                if grumpy[i-X]==1:
                    total-=customers[i-X]
            max_unsat = max(max_unsat, total)
        return ans + max_unsat
