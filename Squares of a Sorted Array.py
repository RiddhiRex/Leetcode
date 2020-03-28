class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        i = 0
        j = 0
        ans = []
        while(i<len(A) and A[i]<0):
            i+=1
        j = i-1
        while(i<len(A) and j>=0):
            if (A[i]**2)>(A[j]**2):
                ans.append(A[j]**2)
                j-=1
            else:
                ans.append(A[i]**2)
                i+=1
        while(i<len(A)):
            ans.append(A[i]**2)
            i+=1
        while(j>=0):
            ans.append(A[j]**2)
            j-=1
        return ans
            
