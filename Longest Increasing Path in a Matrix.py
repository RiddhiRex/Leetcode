class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        r = len(matrix)
        c = len(matrix[0])
        path_table = [[float("-inf") for _ in range(c)] for _ in range(r)]
        self.maxpathlen = 0

        def traverse(i, j, prev):
            if not 0<=i<r or not 0<=j<c or matrix[i][j]<=prev:
                return 0
            if path_table[i][j]!=float("-inf"):
                return path_table[i][j]

            path_table[i][j]=max(traverse(i-1, j, matrix[i][j]),traverse(i+1, j, matrix[i][j]), traverse(i, j-1, matrix[i][j]), traverse(i, j+1, matrix[i][j]) )+1
            
            self.maxpathlen = max(self.maxpathlen , path_table[i][j])
            return  path_table[i][j]


        for i in range(r):
            for j in range(c):
                if path_table[i][j]==float("-inf"):
                    traverse(i, j, float("-inf"))
        return self.maxpathlen
