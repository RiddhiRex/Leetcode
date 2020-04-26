class Solution:
    def numSquares(self, n: int) -> int:
        if n==0:
            return 0
        
        arr = []
        i =1
        while((i*i)<=n):
            arr.append(i*i)
            i+=1
            
        stack = [(1, n)]
        while(stack):
            nxt_stack = set()
            for step_cnt, cur_no in stack:
                if cur_no in arr:
                    return step_cnt
                for num in arr:
                    if cur_no-num>=0:
                        nxt_stack.add((step_cnt+1, cur_no-num))
            stack = nxt_stack
                    
            
                    
