class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = []
        for row in matrix:
            l.extend(row)
        heapq.heapify(l)
        return heapq.nsmallest(k, l)[-1]
