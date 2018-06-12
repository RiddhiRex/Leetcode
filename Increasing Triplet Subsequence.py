class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if(len(nums)< 3):
            return False
        a= None
        b= None
        for n in nums:
            if a is None or a >= n:
                a = n
            elif b is None or b >= n:
                b = n
            else:
                return True
        return False  
