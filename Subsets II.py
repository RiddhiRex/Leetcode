class Solution(object):
    def subsets(self, ans, curr, nums):
        if(len(nums)==0):
            if curr not in ans:
                ans.append(curr)
        else:
            self.subsets(ans, curr, nums[1:])
            self.subsets(ans, curr+[nums[0]], nums[1:])
        return 
    
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==0:
            return []
        ans = []
        self.subsets(ans, [], sorted(nums))
        return ans
