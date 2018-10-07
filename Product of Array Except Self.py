from numpy import prod
class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = []
        for i in range(len(nums)):
            m = itertools.combinations(nums[0:i]+nums[i+1:], len(nums)-1)
            out.append(prod(list(m)))
        return out

    #method2:
    class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_prd=[1]*(len(nums))
        right_prd=1
        
        for i in range(1, len(nums)):
            left_prd[i]=left_prd[i-1]*nums[i-1]  
        
        for i in reversed(range(0, len(nums)-1)):
            right_prd*=nums[i+1]
            left_prd[i]=right_prd*left_prd[i] 
            
        return left_prd
