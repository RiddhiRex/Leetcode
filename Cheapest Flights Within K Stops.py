class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        dic = collections.defaultdict(dict)
        for source, dest, cost in flights:
            dic[source][dest]=cost
        seen = {}
        heap = [(0, src, 0)]  #node, cost, stop number
        
        while(heap):
            cost, node, stop = heapq.heappop(heap)
            if stop>k+1:
                continue
            if node==dst:
                return cost
            
            if node in seen and stop>=seen[node]:
                continue
                
            seen[node]=stop
          
            for dest, tktcost in dic[node].items():
                heapq.heappush(heap, (tktcost+cost,dest, stop+1))
        return -1
                
        
        
