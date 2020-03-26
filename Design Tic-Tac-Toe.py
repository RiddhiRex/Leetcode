class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.board =[[None for i in range(n)] for i in range(n)]
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.board[row][col]=player
        for i in range(1, self.n):
            if self.board[row][i]!=self.board[row][i-1]:
                break
            if i==self.n-1:
                return player
        
        for i in range(1, self.n):
            if self.board[i][col]!=self.board[i-1][col]:
                break   
            if i==self.n-1:
                return player
        
        if row==col:
            for i in range(1, self.n):
                if self.board[i-1][i-1]!=self.board[i][i]:
                    break
                if i==self.n-1:
                    return player
            
        if row+col==self.n-1:
            for i in range(1, self.n):
                if self.board[self.n-i][i-1]!=self.board[self.n-i-1][i]:
                    break
                if i==self.n-1:
                    return player
            
        return 0
            
                    

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
