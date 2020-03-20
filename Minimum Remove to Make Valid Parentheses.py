class Solution(object):
            
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack =[]
        idx_to_rm = set()
        for i , c in enumerate(s):
            if c not in "()":
                continue
            if c=="(":
                stack.append(i)
            elif c==")":
                if len(stack)==0:
                    idx_to_rm.add(i)
                else:
                    stack.pop()

        idx_to_rm = idx_to_rm.union(set(stack))
        ans = []
        for i ,c in enumerate(s):
            if i not in idx_to_rm:
                ans.append(c)
        return "".join(ans)
            
                
                
