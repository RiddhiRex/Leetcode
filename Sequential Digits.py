class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for no in range(1, 10):
            n = no
            nxt = no
            while(n<=high and nxt<10):
                if n>=low:
                    ans.append(n)
                nxt+=1
                n=n*10+nxt
                
        return sorted(ans)
