from itertools import combinations
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mindiff = abs(target - (nums[0]+nums[1]+nums[2]))
        ans = (nums[0]+nums[1]+nums[2])
        tmp = combinations(nums, 3)

        for each in tmp:
            s = 0
            for i in each:  
                s= s+i
            if(s==target):
                return target
            if(abs(s-target))<mindiff:
                ans = s
                mindiff = abs(s-target)
        return ans
        
