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
            
        
        
