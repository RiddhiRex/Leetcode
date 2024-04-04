class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def countdays(limit):
            numdays =1
            cur_weight=0
            for w in weights:
                if cur_weight+w>limit:
                    numdays+=1
                    cur_weight=0
                cur_weight = cur_weight+w
            return numdays
        
        for limit in range(max(weights), sum(weights)+1):
            res = countdays(limit)
            if res<=days:
                return limit


#Solution 2:
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def countdays(limit):
            numdays =1
            cur_weight=0
            for w in weights:
                if cur_weight+w>limit:
                    numdays+=1
                    cur_weight=0
                cur_weight = cur_weight+w
            return numdays
        
        l = max(weights)
        r = sum(weights)
        while(l<r):
            mid = l + (r-l)//2
            
            res = countdays(mid)
            if res<=days:
                r = mid
            else:
                l=mid+1
        return l
        
                
