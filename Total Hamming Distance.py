class Solution:
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor=0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                b = nums[i]^nums[j]
                bit =0
                while(b):
                    if(b&1):
                        bit=bit+1
                    b = b>>1
                xor = xor + bit
        return xor
    
    
#method 2: assume 32 bit length and compare ith bit of all numbers and if ith bit is set, increment cnt.
#those for which ith bit is not set is found by n-cnt.
#product both and add to sum
import itertools
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        n = len(nums)
        for i in range(32):
            cnt=0
            for no in nums:
                if(no & (1<<i)):
                    cnt+=1
            sum+= (cnt*(n-cnt))
        return sum
        
