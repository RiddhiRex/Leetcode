class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations, reverse=True)
        h_index = 0
        for i in range(len(citations)):
            print(citations[i])
            if ((i+1)<=citations[i]):
                h_index=i+1
            else:
                break
        return h_index
        
        
        
        
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        n = len(citations)
        print(citations)

        for i in range(n):
            if citations[i] < i + 1:
                return i

        return n
        
        
        
        
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
                
        
