class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        l = []
        operators = ["+", "-", "*", "/"]
        for each in tokens:
            if each not in operators:
                l.append(int(each))
            else:
                print(each)
                t2 = l.pop()
                t1 = l.pop()
                if(each=='+'):
                    l.append(t1+t2)
                elif(each=='-'):
                    l.append(t1-t2)
                elif(each=='*'):
                    l.append(t1*t2)
                elif(each=='/'):
                    l.append(t1//t2)
        return l.pop()
        
