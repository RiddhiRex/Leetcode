class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0]*len(T)
        #Stack will contain index of days hottest to coldest
        #next occurrence of a warmer temperature is simply the top index in the stack.
        stack = []
        #traverse from end to start
        for i in range(len(T)-1, -1, -1):
            #while top of stack is < T[i], remove it
            while len(stack)>0 and T[i]>=T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i]=stack[-1]-i
            stack.append(i)
        return ans
