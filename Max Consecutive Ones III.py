class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        maxlen = 0
        left = 0
        zeros=0
        for right in range(len(A)):
            if A[right]==0:
                zeros+=1
            while(zeros>K):
                if A[left]==0:
                    zeros-=1
                left+=1
            maxlen = max(maxlen, right-left+1)
        return maxlen
