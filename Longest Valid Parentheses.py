class Solution(object):
    def isValid(self, s):
        if len(s)==0:
            return True
        c=0
        for each in s:
            if each=="(":
                c+=1
            else:
                c-=1
                if c<0:
                    return False
        if c!=0:
            return False
        else:
            return True
        
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        invalid = -1
        maxlen = 0
        for i in range(len(s)):
            if s[i]=="(":
                stack.insert(0, i)
            elif len(stack)==0:
                invalid=i
            else:
                stack.pop(0)
                if len(stack)==0:
                    maxlen=max(maxlen, i-invalid)
                else:
                    maxlen=max(maxlen, i-stack[0])
        return maxlen
