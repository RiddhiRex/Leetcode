from itertools import permutations, product
class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if(len(S))==0:
            return [S]
        rest = self.letterCasePermutation(S[1:])
        if(S[0].isalpha()):
            return [S[0].lower() +i for i in rest] + [S[0].upper() +i for i in rest]
        else:
            return [S[0]+i for i in rest]
