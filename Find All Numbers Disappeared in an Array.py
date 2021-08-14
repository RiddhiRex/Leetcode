class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if(len(nums)<=1):
            return nums
        for i in range(1, len(nums)+1):
            if i in nums:
                while i in nums:
                    nums.remove(i)
            else:
                nums.append(i)
        return nums

    
    class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        return list(set(range(1, n+1))-set(nums))
