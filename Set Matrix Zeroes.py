class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        i=0
        row=[]
        col=[]
        for each in matrix:
            if 0 in each:
                row.append(i)
                for k in range(len(each)):
                    if each[k]==0:
                        col.append(k)
            i=i+1
        for i in range(len(matrix)+1):
            if i in row:
                for j in range(len(matrix[0])):
                    matrix[i][j]=0
        for i in range(len(matrix[0])+1):
            if i in col:
                for j in range(len(matrix)):
                    matrix[j][i]=0
        
