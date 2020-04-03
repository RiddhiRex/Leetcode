class Solution:
    def maximumSwap(self, num: int) -> int:
        nos = [n for n in str(num)]
        if nos==sorted(nos)[::-1]:
            return num
        #dictionary to mark the idx of last occurance of a digit in the number
        d_lastpos = {}
        for i, no in enumerate(nos):
            d_lastpos[no]=i
        for i, no in enumerate(nos):
            for j in range(9, int(no), -1):
                #get fucntion returns val if given key is found, else returns None
                pos = d_lastpos.get(str(j), None)
                if pos!=None and pos>i:
                    tmp = nos[i]
                    nos[i]=nos[d_lastpos[str(j)]]
                    nos[d_lastpos[str(j)]] =tmp
                    return int("".join(nos))
        return int("".join(nos))
                    
                    
        
            
        
        
