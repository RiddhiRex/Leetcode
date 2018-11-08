class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row=len(obstacleGrid)
        col = len(obstacleGrid[0])
        path=[[0]*col for i in range(row)]
        if obstacleGrid[0][0]==1 or obstacleGrid[-1][-1]==1:
            return 0
        path[0][0]=1
        for i in range(1, row):
            if obstacleGrid[i][0]==0:
                path[i][0]=path[i-1][0]
  
        for j in range(1, col):
            if obstacleGrid[0][j]==0:
                path[0][j]=path[0][j-1]
      
        for i in range(1, row):
            for j in range(1, col):
                if(obstacleGrid[i][j]==0):
                    path[i][j]=path[i-1][j]+path[i][j-1]
   
        return path[-1][-1]
        
