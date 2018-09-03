class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        l=[]
        for each in A:
            l.append(B.index(each))
        return l
        
