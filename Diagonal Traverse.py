'''
We use a flag 'goingup' to decide whether we need to go upward direction or downward direction. 
We set goingup = true initially that first we are going upward.
If goingup = 1 then start printing elements by incrementing column index and decrementing the row index.
Similarly if goingup = 0, then decrement the column index and increment the row index.
Do this till all the elements get traversed
'''
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        row = len(matrix)
        col = len(matrix[0])
        going_up=True
        visited_cnt=0
        r =0
        c=0
        while(visited_cnt<(row*col)):
            if going_up==True:
                while(0<=r<row and 0<=c<col):
                    #decrement the row, increment the column
                    ans.append(matrix[r][c])
                    r-=1
                    c+=1
                    visited_cnt+=1
                if r<0 and c<=col-1:
                    r=0
                if c==col:
                    r=r+2
                    c=c-1
                    
            else:
                while(0<=r<row and 0<=c<col):
                    #increment the row, decrement the col
                    ans.append(matrix[r][c])
                    r+=1
                    c-=1
                    visited_cnt+=1
                if c<0 and r<=row-1:
                    c=0
                if r==row:
                    r=r-1
                    c=c+2
            going_up = not going_up
        return ans
                    
                
