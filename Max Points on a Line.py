class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if(len(points)<3):
            return len(points)
        max_pts = 0
        for i, pt1 in enumerate(points):
            slope_dict = collections.defaultdict(int)
            same_pt =1
            for j, pt2 in enumerate(points):
                if i==j:
                    continue
                else:
                    if pt1[0]==pt2[0] and pt1[1]==pt2[1]:
                        same_pt+=1
                    else:
                        if(pt1[0]==pt2[0]):
                            slope = float('inf')
                        else:
                            slope = (pt2[1]-pt1[1])/(pt2[0]-pt1[0])
                    slope_dict[slope]+=1
            max_pts = max(max_pts, same_pt+max(slope_dict.values()))
        return max_pts
            
        
