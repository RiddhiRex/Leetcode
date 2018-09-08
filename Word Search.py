class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if self.dfs(board, i, j, word) is True:
                        return True
        return False
    
    def dfs(self, board, row, col, w):
        if(len(w)==0):
            print("here")
            return True
        if(row<0 or col<0 or row>=len(board) or col>=len(board[0]) or board[row][col]!=w[0]):
            return False
        tmp = board[row][col]
        board[row][col]="#"
        
        result = self.dfs(board, row+1, col, w[1:]) or self.dfs(board, row-1, col, w[1:]) or self.dfs(board, row, col+1, w[1:]) or self.dfs(board, row, col-1, w[1:])
        
        board[row][col]=tmp
        return result
        
        
