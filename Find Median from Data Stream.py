class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        #Store the smaller half of numbers
        self.minheap = []
        #Store the higher half of the numbers
        self.maxheap = []
        

    def addNum(self, num: int) -> None:
        #Inserting number into appropriate heap.
        
        # insert negative of the num into maxheap. 
        if len(self.maxheap)==0 or num <= -self.maxheap[0]:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)
            
        #Balancing the two heaps.
        #maxheap len can be greater than minheap by atmost 1. 
        #If minheap size is larger than maxheap, then move the root of minheap to maxheap.
        if len(self.maxheap)-len(self.minheap)>1:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
        elif len(self.minheap)-len(self.maxheap)>0:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

    def findMedian(self) -> float:
        if len(self.minheap)==len(self.maxheap):
            return (-self.maxheap[0]+self.minheap[0])/2
        else:
            return -self.maxheap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
