class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=[]
        i=0
        while i < len(s):
            if s[i].isdigit():
                l.append(int(s[i]))
            elif s[i] =="/":
                n = l.pop()
                i=i+1
                n = int(n)//int(s[i])
                l.append(n)
            elif s[i] == "*":
                n = l.pop()
                i=i+1
                n = int(n)*int(s[i])
                l.append(n)
            else:
                l.append(s[i])
            i=i+1
        print(l, len(l))
        while(len(l)>1):
            n1 = l.pop(0)
            op = l.pop(0)
            n2 = l.pop(0)
            if(op=="+"):
                n1 = int(n1)+int(n2)
            elif(op=="-"):
                n1=int(n1)-int(n2)
            l.insert(0, n1)
        return l[0]
                
