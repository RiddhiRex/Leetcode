class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
                return "0"
            elif grid[i][j]==0:
                return "0"
            grid[i][j]=0
            ans = "1"
            direction = {'u':[1,0],'d':[-1,0],'l':[0,-1],'r':[0,1]}
            for d, (x,y) in direction.items():
                    ans += dfs(grid, i+x, j+y)
                                                 
            return ans
            
        shape = set()
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    dtn = dfs(grid, i, j)
                    shape.add(dtn)
        return len(shape)
                    
