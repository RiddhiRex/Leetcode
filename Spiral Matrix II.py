class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        if n==0:
            return []
        left=0
        top=0
        matrix=[[0]*n for i in range(n)]
        right=len(matrix[0])-1
        bottom=len(matrix)-1
        ans=[]
        j=1
        while(left<=right and top<=bottom):
            for i in range(left, right+1):
                matrix[top][i]=j
                j+=1
            
            for i in range(top+1, bottom):
                matrix[i][right]=j
                j+=1
           
            for i in reversed(range(left, right+1)):
                if(top<bottom):
                    matrix[bottom][i]=j
                    j+=1
            
            for i in reversed(range(top+1, bottom)):
                if left<right:
                    matrix[i][left]=j
                    j+=1
           
            left+=1
            right-=1
            top+=1
            bottom-=1
        return matrix
        
