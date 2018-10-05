class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(itertools.permutations(nums, len(nums)))

#solution 2:
class Solution(object):
    def permutation(self, ans, nums, path):
        if len(nums)==0:
            ans.append(path)
            return
        for i in range(len(nums)):
            self.permutation(ans, nums[:i]+nums[i+1:], path+[nums[i]])
        return 
    
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==0:
            return []
        ans = []
        self.permutation(ans, nums, [])
        return ans
