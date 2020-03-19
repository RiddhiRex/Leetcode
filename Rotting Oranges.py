class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = len(grid)
        c = len(grid[0])
        steps = 0
        fresh = 0
        rottenq = []
        for i in range(r):
            for j in range(c):
                if grid[i][j]==2:
                      rottenq.append((i,j,0))
                elif grid[i][j]==1:
                      fresh += 1
                        
        print(fresh, rottenq)
        
        while len(rottenq)>0:
            i, j, mvs=rottenq.pop(0)
            for x,y in [(1, 0),(-1,0),(0,1),(0,-1)]: 
                if ((x+i>=0 and y+j>=0 and x+i<r and y+j<c) and grid[x+i][y+j]==1):
                    fresh-=1
                    grid[x+i][y+j]=2
                    rottenq.append((x+i,y+j,mvs+1))
                    steps = max(steps, mvs+1)
                   
        if fresh > 0:
            return -1
        else:
            return steps
        
