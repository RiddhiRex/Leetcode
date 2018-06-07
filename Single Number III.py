class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = []
        for each in nums:
            if each in n:
                n.remove(each)
            else:
                n.append(each)
        return n
