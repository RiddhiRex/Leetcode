class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if(len(matrix)==0 or len(matrix[0])==0):
            return False
        for each in matrix:
            if each[-1] >=target:
                for i in each:
                    if i==target:
                        return True
        return False
                
