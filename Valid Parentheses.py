class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c=[]
        for i in s:
            if i=='(' or i=='{' or i=='[':
                c.append(i)
            if i==')':
                if(len(c)<1):
                    return False
                if(c.pop()!='('):
                    return False
            if i=='}':
                if(len(c)<1):
                    return False
                if(c.pop()!='{'):
                    return False 
            if i==']':
                if(len(c)<1):
                    return False
                if(c.pop()!='['):
                    return False
        if(len(c)==0):
            return True
        else:
            return False
            
