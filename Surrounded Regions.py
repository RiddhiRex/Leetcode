class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board==[]:
            return
        r = len(board)
        c = len(board[0])
        def dfs(x, y):
            if x<0 or y<0 or x>r-1 or y>c-1 or board[x][y]!='O':
                return
            board[x][y]='*'
            dfs(x-1, y)
            dfs(x, y-1)
            dfs(x+1, y)
            dfs(x, y+1)
            return
        
        for i in range(r):
            dfs(i, 0)
            dfs(i, c-1)
        for j in range(c):
            dfs(0, j)
            dfs(r-1, j)
        for i in range(r):
            for j in range(c):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='*':
                    board[i][j]='O'
        return 
