import math,operator
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        ans = []
        for p in points:
            x, y = p
            d =  (x*x)+(y*y)
            ans.append((d, p))
            
        ans.sort(key=operator.itemgetter(0))
        print(ans)
        a = [pt for d, pt in ans]
        return a[0:K]
