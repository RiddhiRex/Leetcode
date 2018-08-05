class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        for i in range((2**n)):
            ans.append(i>>1^i)
        return ans
