class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        r = 0
        c = cols-1 
        #search from top right corner
        while(r<rows and c>=0):
            if matrix[r][c]==target:
                return True
            if matrix[r][c]>target:
                c-=1
            else:
                r+=1
        return False
