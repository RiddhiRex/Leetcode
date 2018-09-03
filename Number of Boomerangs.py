import collections
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        cnt=0
        
        for i in range(len(points)):
            dist = collections.defaultdict(int)
            for j in range(len(points)):
                if i==j:
                    continue
                dx = points[i][0]-points[j][0]
                dy=points[i][1]-points[j][1]
                dist[(dx**2 + dy**2)]+=1       
            for k, v in dist.items():
                if v>1:
                    cnt=cnt+(v*(v-1))
        return cnt

        
        
