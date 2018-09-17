class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea=0
        i=0
        j=len(height)-1
        while(i<j):
            area = min(height[i], height[j])*(j-i)
            maxarea =max(maxarea, area)
            if(height[i]<height[j]):
                i+=1
            else:
                j-=1
        return maxarea
