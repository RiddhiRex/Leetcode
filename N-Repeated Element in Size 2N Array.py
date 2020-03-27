class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        d = collections.Counter(A)
        return sorted(d.items(), key = operator.itemgetter(1))[-1][0]
        
