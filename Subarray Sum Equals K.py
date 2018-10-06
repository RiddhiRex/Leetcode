class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        cnt=0
        for i in range(len(nums)):
            sum=nums[i]
            if sum==k:
                cnt+=1
            for j in range(i+1, len(nums)):
                sum=sum+nums[j]
                if(sum==k):
                    cnt+=1
        return cnt
                
            
