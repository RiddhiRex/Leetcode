class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for r, row in enumerate(matrix):
            for c, col_val in enumerate(row):
                if r>0 and c>0 and matrix[r-1][c-1]!= col_val:
                    return False
        return True
        
