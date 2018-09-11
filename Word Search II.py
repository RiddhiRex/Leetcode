import copy
class Solution(object):
    def traverse(self, board, w, row, col, i, j):
        idx=1
        brd=copy.deepcopy(board)
        while(idx<len(w)):
            brd[i][j]="*"
            if(i>0 and brd[i-1][j]==w[idx]):
                i-=1
            elif(i<(row-1) and brd[i+1][j]==w[idx]):
                i+=1
            elif(j<(col-1) and brd[i][j+1]==w[idx]):
                j=j+1
            elif(j>0 and brd[i][j-1]==w[idx]):
                j-=1
            else:
                return False
            idx+=1   
        return True
                
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        row=len(board)
        col=len(board[0])
        ans = []
        for each in words:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j]==each[0]:
                        if(self.traverse(board, each, row, col, i, j) is True):
                            if each not in ans:
                                ans.append(each)
                                
        return ans
                    
                    
