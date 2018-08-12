class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid)==0:
            return 0
        row= len(grid)
        col= len(grid[0])
        cnt=0
        for i in range(row):
            for j in range(col):
                if(grid[i][j]=="1"):
                    self.dfs(grid, row, col, i, j)
                    cnt=cnt+1
                    
        return cnt
    
    def dfs(self, grid, row, col, i, j):
        if(grid[i][j]=="0"):
            return
        grid[i][j]="0"
        if(i>0):
            self.dfs(grid, row, col, i-1, j)
        if(i!=row-1):
            self.dfs(grid, row, col, i+1, j)
        if(j>0):
            self.dfs(grid, row, col, i, j-1)
        if(j!=col-1):
            self.dfs(grid, row, col, i, j+1)
           
