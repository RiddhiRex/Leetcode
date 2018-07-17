class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if(len(matrix)==0 or len(matrix[0])==0):
            return False
        if(len(matrix)==1 and len(matrix[0])==1):
            if(matrix[0][0]==target):
                return True
            else:
                return False
        cntrow = len(matrix)
        cntcol = len(matrix[0])
        row=0
        col = cntcol-1
        while(row<cntrow and col>=0):
            if(matrix[row][col]==target):
                return True
            elif(matrix[row][col]>target):
                col=col-1
            else:
                row=row+1
        return False
             
                
