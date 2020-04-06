class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stackcnt = 0
        ans = 0
        for i in S:
            if i=="(":
                stackcnt+=1
            else:
                stackcnt-=1
                if stackcnt<0:
                    ans+=1
                    stackcnt+=1
        return ans+stackcnt
                
