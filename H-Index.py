class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        ans = []
        if(len(citations)==0):
            return 0
        if(len(citations)==1 and citations[0]>=1):
            return 1

        for i in reversed(range(1, len(citations)+1)):
            cnt=0
            for j in range(len(citations)):
                if citations[j]>=i:
                    cnt=cnt+1 
            if cnt>=i:
                return i
        return 0
                
        
