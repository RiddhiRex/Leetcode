class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        for no in A:
            if no%2==0:
                even.append(no)
            else:
                odd.append(no)
        return even+odd
        
