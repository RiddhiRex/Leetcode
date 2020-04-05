 #Solution 1:
    class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        l = []
        v = ['a','e','i','o','u']
        i=1
        for w in list(S.split(" ")):
            if w[0].lower() in v:
                wrd=w+"ma"+('a'*i)
            else:
                wrd=w[1:]+w[0]+"ma"+('a'*i)
            i+=1
            l.append(wrd)
            print(wrd)
        return " ".join(l)
            
#Solution 2:
class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels=list("aeiouAEIOU")
        wrds = S.split(" ")
        for i, w in enumerate(wrds):
            if w[0] not in vowels:
                w = w[1:]+w[:1]
            wrds[i]=w+"ma"+(i+1)*"a"
        return " ".join(wrds)
        
