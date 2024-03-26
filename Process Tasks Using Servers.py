class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        available = []  # heap of available servers (weight, index)
        busy = []       # heap of busy servers (end_time, weight, index)
        res = []        # stores the result
        
        for i, w in enumerate(servers):
            heapq.heappush(available, (w, i))
        
        time = 0
        for i, t in enumerate(tasks):
            while busy and busy[0][0] <= time:  # release busy servers whose tasks have finished
                end_time, weight, idx = heapq.heappop(busy)
                heapq.heappush(available, (weight, idx))
                
            if not available:  # no available servers, fast forward time
                time = busy[0][0]
                continue
            
            weight, idx = heapq.heappop(available)
            heapq.heappush(busy, (time + t, weight, idx))
            res.append(idx)
            time += 1
        
        return res
