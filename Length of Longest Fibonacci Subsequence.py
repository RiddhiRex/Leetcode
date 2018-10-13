import collections
class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        maxlen=0
        cnt=0
        d = set(A)
        for i in range(0, len(A)):
            for j in range(i+1, len(A)):
                a=A[i]
                b=A[j]
                cnt=2
                while (a+b in d):
                    c=a+b
                    a=b
                    b=c
                    cnt+=1
                if cnt!=2:
                    maxlen=max(maxlen, cnt)
                    
        return maxlen
            
        
