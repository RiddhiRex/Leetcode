class Solution(object):
    def traverse(self, grid, row, col, i, j):
        if(grid[i][j]==0):
            return 0
        grid[i][j]=0
        cnt=1
        if(i>0):
            cnt+=self.traverse(grid, row, col, i-1, j)
        if(i!=row-1):
            cnt+=self.traverse(grid, row, col, i+1, j)
        if(j>0):
            cnt+=self.traverse(grid, row, col, i, j-1)
        if(j!=col-1):
            cnt+=self.traverse(grid, row, col, i, j+1)
        return cnt
    
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col=len(grid[0])
        maxarea=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==1):
                    cnt = self.traverse(grid, row, col, i, j)
                    maxarea = max(maxarea, cnt)
        return maxarea
                    
                
        
