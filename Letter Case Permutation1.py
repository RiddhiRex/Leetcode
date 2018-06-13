from itertools import permutations, product
class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        return list(map(''.join, product(*(set((c.upper(), c.lower()))
                                       for c in S))))
