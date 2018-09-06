class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        r1_b = rec1[0]
        r1_l = rec1[1]
        r1_t = rec1[2]
        r1_r = rec1[3]
        
        r2_b = rec2[0]
        r2_l = rec2[1]
        r2_t = rec2[2]
        r2_r = rec2[3]
        if(max(r1_l, r2_l)<min(r1_r, r2_r) and max(r1_b, r2_b)<min(r1_t, r2_t)):
            return True
        else:
            return False
