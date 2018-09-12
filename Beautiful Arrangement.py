import itertools
class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        no=[]
        cnt=0

        for i in range(1, N+1):
            no.append(i)
        l = itertools.permutations(no)
        for each in l:
            flag=False
            for i in range(0, len(each)):
                if each[i]%(i+1)!=0 and (i+1)%each[i]!=0:
                    flag=True
                    break
            if flag is False:
                cnt+=1
        return cnt
                    
        
