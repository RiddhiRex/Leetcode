class Solution:
    def smallestSubsequence(self, s: str) -> str:
        dict = {}
        for idx, i in enumerate(s):
            dict[i]=idx
        stack = []
        seen = set()
        minlen = float("inf")
        distinct_cnt = len(dict)
        for idx, i in enumerate(s):
            if i not in seen:
                while(stack and stack[-1]>i and dict[stack[-1]]>idx):
                    seen.remove(stack[-1])
                    stack.pop()
                stack.append(i)
                seen.add(i)
            
        return "".join(stack)

