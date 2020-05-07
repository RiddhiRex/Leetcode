class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
            trips.sort(key=lambda x:x[1])
            print(trips)
            start = []
            end = []
            for x, y, z in trips:
                start.append((x, y))
                end.append((x, z))

            start.sort(key=lambda x:x[1])
            end.sort(key=lambda x:x[1])

            cur_cap = 0
            start_idx = 0
            end_idx = 0
            while(end_idx<len(trips)):
                if start_idx<len(trips) and start[start_idx][1]<end[end_idx][1]:
                    cur_cap+=start[start_idx][0]
                    start_idx+=1
                else:
                    cur_cap-=end[end_idx][0]
                    end_idx+=1

                if cur_cap>capacity:
                    return False
            return True
        
