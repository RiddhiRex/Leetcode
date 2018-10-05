class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = []
        for each in range(len(nums)+1):
                l.extend(list(itertools.combinations(nums, each)))
        return l
    
  #solution 2:
class Solution(object):
    def subsetCreation(self, ans, curr, nums):
        if len(nums)==0:
            ans.append(curr)
            return
        self.subsetCreation(ans, curr, nums[1:])
        self.subsetCreation(ans, curr+[nums[0]], nums[1:])
        return
    
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if(len(nums))==0:
            return []
        ans = []
        self.subsetCreation(ans, [], nums)
        return ans
        
