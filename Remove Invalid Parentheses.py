class Solution(object):
    def isValid(self, st):
        c = 0
        for each in st:
            if each=="(":
                c+=1
            elif each==")":
                c-=1
                if c<0:
                    return False
        if c==0:
            return True
        else:
            return False
        
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        currs = [s]
        while(True):
            #to filter the strings that have returned True in the self.isValid function
            validst = filter(self.isValid, currs)
            if len(validst)>0:
                return validst
            t=set()
            for each in currs:
                for i in range(len(each)):
                    t.add(each[:i]+each[i+1:])
            currs = t
            
            
