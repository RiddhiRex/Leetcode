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
                
  #method 2:
import collections
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        result=0
        d=collections.defaultdict(int)
        d[0]=1
        total_sum=0
        for i in range(len(nums)):
            total_sum+=nums[i]
            result+=d[total_sum-k]
            d[total_sum]+=1

        return result  

    Solution 2 copy
    class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = 0
        cnt = 0
        sum_dict = collections.defaultdict(int)
        sum_dict[0]=1

        for i in range(len(nums)):
            total+=nums[i]
            cnt+=sum_dict[total-k]
            sum_dict[total]+=1

        return cnt
