class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for i in range(len(board)):
            l1=[]
            l2=[]
            for j in range(len(board[i])):
                if board[j][i] !=".":
                    l1.append(board[j][i])
                if board[i][j] !=".":
                    l2.append(board[i][j])               
            if len(l1)!=len(set(l1)) or len(l2)!=len(set(l2)):
                return False
            
            for i in range(0,3):
                l1=[]
                l2=[]
                l3=[]
                for j in range(0,3):
                    if board[i*3][j] !=".":
                        l1.append(board[i*3][j])
                    if board[i*3+1][j] !=".":
                        l1.append(board[i*3+1][j])
                    if board[i*3+2][j] !=".":
                        l1.append(board[i*3+2][j])

                    if board[i*3][j+3] !=".":
                        l2.append(board[i*3][j+3])
                    if board[i*3+1][j+3] !=".":
                        l2.append(board[i*3+1][j+3])
                    if board[i*3+2][j+3] !=".":
                        l2.append(board[i*3+2][j+3])
                        
                    if board[i*3][j+6] !=".":
                        l3.append(board[i*3][j+6])
                    if board[i*3+1][j+6] !=".":
                        l3.append(board[i*3+1][j+6])
                    if board[i*3+2][j+6] !=".":
                        l3.append(board[i*3+2][j+6])          
                if len(l1)!=len(set(l1)) or len(l2)!=len(set(l2)) or len(l3)!=len(set(l3)):
                    return False 
        return True
            
            

        
        
                
        
