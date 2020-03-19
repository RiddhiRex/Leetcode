class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        l = len(words)
        o = {w: i for i,w in enumerate(order)}
        for i in range(len(words)-1):
            w1= words[i]
            w2= words[1+i]
            
            for i in range(min(len(w1), len(w2))):
                if w1[i]!=w2[i]:
                     if o[w1[i]]>o[w2[i]]:
                            return False
                     else:
                        if o[w1[i]]<o[w2[i]]:
                                break
                     
                         
            if w2==w1[0:len(w2)] and len(w1)>len(w2):
                        return False
            
        return True
                
