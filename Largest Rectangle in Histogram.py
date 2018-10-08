class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        maxarea=0
        i=0
        while(i<=len(heights)):
            if len(stack)==0 or (i<len(heights) and heights[i]>heights[stack[0]]):
                stack.insert(0, i)
                i+=1
            else:
                popped=stack.pop(0)
                if(len(stack)==0):
                    maxarea=max(maxarea, heights[popped]*i)
                else:
                    maxarea=max(maxarea, heights[popped]*(i-stack[0]-1))
        return maxarea
            
