class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        D = list(S)
        for j in range(len(shifts)):
            if shifts[j]>26:
                shifts[j]=shifts[j]%26
            for i in range(j+1):
                n = ord(D[i])+shifts[j]
                if(n<=122):
                    D[i]=chr(n)
                else:
                    D[i] = chr((n%122)+96)
        return ("".join(D))
        
