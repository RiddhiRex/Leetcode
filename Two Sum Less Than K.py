class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        i = 0
        j = len(A)-1
        maxsum = -1
        A = sorted(A)
        while (i<j):
            if A[i]+A[j]<K:
                maxsum = max(maxsum, A[i]+A[j]) 
                i+=1
            else:
                j-=1
        return maxsum
