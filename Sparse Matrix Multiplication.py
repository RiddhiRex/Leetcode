class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(A)==0 and len(B)==0:
            return [[]]
        
        ra = len(A)
        cb = len(B[0])
        rb = len(B)
        
        ans = [[0 for i in range(cb)] for j in range(ra)]
        print(ans)
        for i in range(ra):
            for j in range(rb):
                if A[i][j]!=0:
                    for k in range(cb):
                         ans[i][k] +=A[i][j]*B[j][k]
        return ans
        
