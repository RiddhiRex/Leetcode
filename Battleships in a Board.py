class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if len(board)==0 or len(board[0])==0:
            return 0
        r = len(board)
        c = len(board[0])
        cnt = 0
        for i in range(r):
            for j in range(c):
                if board[i][j]=="X":
                    #Condition to check if it is part of ship that is already counted
                    if(i!=0 and board[i-1][j]=="X") or (j!=0 and board[i][j-1]=="X"):
                        continue
                    cnt+=1
                    
        return cnt
