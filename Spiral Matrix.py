class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix)==0:
            return []
        left=0
        top=0
        right=len(matrix[0])-1
        bottom=len(matrix)-1
        ans=[]
        while(left<=right and top<=bottom):
            for i in range(left, right+1):
                ans.append(matrix[top][i])
            for i in range(top+1, bottom):
                ans.append(matrix[i][right])
            for i in reversed(range(left, right+1)):
                if(top<bottom):
                    ans.append(matrix[bottom][i])
            for i in reversed(range(top+1, bottom)):
                if left<right:
                    ans.append(matrix[i][left])
            left+=1
            right-=1
            top+=1
            bottom-=1
            
        return ans
            
