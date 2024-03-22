class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        res = 0
        for i in s:
            if i=="(":
                stack.append(i)
            else:
                if(len(stack)>0):
                    stack.pop()
                else:
                    res+=1
        res +=len(stack)
        return res
        
        
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
                
