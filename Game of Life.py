class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board)==0:
            return
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                cnt = 0
                for I in range(max(0,i-1), min(i+2, row)):
                    for J in range(max(0, j-1), min(j+2, col)):
                        if(board[I][J]&1):
                            cnt=cnt+1
                if ((board[i][j]==1 and cnt==4) or cnt==3):
                    board[i][j]|=2 #set live cells. Doing OR with 10
                    
                    
        for i in range(row):
            for j in range(col):
                board[i][j]>>=1
                
