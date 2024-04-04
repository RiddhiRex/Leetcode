class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]; max_length = 0
        
        for b in s:
        	if b == "(":
        		stack.append(0)
        	else:
        		if len(stack) > 1:
        			val = stack.pop()
        			stack[-1] += val + 2
        			max_length = max(max_length, stack[-1])
        		
        		else:
        			stack = [0]
        return max_length  






#Solution 2
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
