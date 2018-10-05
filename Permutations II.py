import itertools
class Solution(object):
    def permute(self, ans, nums, path):
        if len(nums)==0:
            ans.append(path)
            return ans
        dic={}
        for each in nums:
            dic[each]=1
        for i in range(len(nums)):
            if  dic[nums[i]]==1:
                self.permute(ans, nums[:i]+nums[i+1:], path+[nums[i]])
                dic[nums[i]]-=1
        return ans
            
            
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==0:
            return []
        return self.permute([], nums, [])
        

        
        
        
