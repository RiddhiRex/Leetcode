class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        i=0
        ans =0
        while(i<len(points)):
            j=i+1
            right_end=points[i][1]
            while(j<len(points) and points[j][0]<=right_end):
                right_end = min(right_end, points[j][1])
                j+=1
            ans+=1
            i=j
        return ans
