"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
 

After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4  
"""
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        wall = -1
        gate = 0
        unknown = 2147483647
        cur_pos = []
        r = len(rooms)
        c= len(rooms[0])
        for i in range(r):
            for j in range(c):
                if rooms[i][j]==gate:
                    cur_pos.append((i,j))
        
        while(len(cur_pos)>0):
            nxt_pos=[]
            for x, y in cur_pos:
                cur_dist = rooms[x][y]
                for i, j in [[-1,0],[0,-1],[1,0],[0,1]]:
                    if r>x+i>0 and c>y+j>0 and rooms[x+i][y+j]==unknown:
                        rooms[x+i][y+j]=cur_dist+1
                        nxt_pos.append((x+i, y+j))
            cur_pos = nxt_pos
        return rooms
        

INF = 2147483647
m = [[INF, -1, 0, INF],[INF, INF, INF, -1],[INF, -1, INF, -1],[0, -1, INF, INF]]
r = Solution()
n = r.wallsAndGates(m)
print(n)
