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
