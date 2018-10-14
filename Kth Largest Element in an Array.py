class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums, reverse=True)[k-1:k][0]

    
 #method 2
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]
    
    #method3:
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        length=len(nums)
        heapq.heapify(nums)
        i=0
        while(i<(length-k)):
            heapq.heappop(nums)
            i+=1
        return heapq.heappop(nums)
    
    #method4:
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(len(nums)):
            nums[i]=-nums[i]
            
        heapq.heapify(nums)
        i=1
        while(i<k):
            heapq.heappop(nums)
            i+=1
        return -heapq.heappop(nums)
        
        
        
