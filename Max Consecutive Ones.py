class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        sum=0
        for each in nums:
            if(each==1):
                sum=sum+1
            else:
                if(max<sum):
                    max = sum
                    sum=0
                else:
                    sum=0
        if(max!=sum and sum>max):
            max=sum
        return max
