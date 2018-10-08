class Solution(object):
    def histogram_area_fn(self, area):
        maxarea=0
        stack = []
        i=0
        while(i<=len(area)):
            if len(stack)==0 or (i<len(area) and area[i]>area[stack[0]]):
                stack.insert(0, i)
                i+=1
            else:
                popped_idx=stack.pop(0)
                if(len(stack)==0):
                    maxarea=max(maxarea, area[popped_idx]*i)
                else:
                    maxarea=max(maxarea, area[popped_idx]*(i-stack[0]-1))
        return maxarea
    
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if(len(matrix))==0 or len(matrix[0])==0:
            return 0
        row_cnt=len(matrix)
        col_cnt=len(matrix[0])
        area = [int(i) for i in matrix[0]]
        max_area=0
        for i in range(0, row_cnt):
            if i!=0:
                for j in range(col_cnt):
                        if(int(matrix[i][j])!=0):
                            area[j]=area[j]+int(matrix[i][j])
                        else:
                            area[j]=0

            max_area=max(max_area, self.histogram_area_fn(area))
        return max_area                
            
        
