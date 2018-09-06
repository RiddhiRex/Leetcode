class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area_r1 = (D-B) * (C-A)
        area_r2 = (H-F) * (G-E)
        if(max(A, E)<min(C, G) and max(B,F)<min(D, H)):
            area_Intersect = (max(B, F)-min(D, H))*(max(A, E)-min(C, G))
            return area_r1+area_r2-area_Intersect
        else:
            return area_r1+area_r2
