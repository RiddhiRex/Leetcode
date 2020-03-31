class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        last_time = 0
        ans = [0 for i in range(n)]
        for log in logs:
            pid, typ, time = log.split(":")
            pid = int(pid)
            time=int(time)
            if typ=="start":
                if stack:
                    ans[stack[-1]] += time-last_time
                stack.append(pid)
                last_time = time
            else:
                ans[stack[-1]] += time-last_time+1
                stack.pop()
                last_time = time+1
                
        return ans
                
                
