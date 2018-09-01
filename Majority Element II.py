import collections
import math
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if(len(nums)<=1):
            return nums
        n = collections.Counter(nums)
        minval = math.floor(len(nums)/3)
        ans=[]
        for k, v in n.items():
            if v>minval:
                ans.append(k)
        return ans
        
