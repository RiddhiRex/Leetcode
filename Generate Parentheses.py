class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []

        def generate(s, open, close):
            if len(s)==2*n:
                self.ans.append(s)
            if(open<n):
                generate(s+"(", open+1, close)
            if(close<open):
                generate(s+")", open, close+1)
        generate("", 0 , 0)
        return self.ans
        
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l = ""
        f = []
        p =[]
        for i in range(n):
            l=l+"()"
        k = itertools.permutations(l)
        for each in k:
            if each not in p:
                p.append(each)
        for each in p:
            o=0
            c=0
            for i in each:
                if(i=="("):
                    o=o+1
                elif(i==")"):
                    c=c+1
                if(c>o):
                    break
            if(c==o):
                if "".join(each) not in f:
                    f.append("".join(each))
        return (f)            
        
