#Logic from https://www.youtube.com/watch?v=-AMHUdZc9ss
import itertools
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l=[]
        nums=sorted(nums)

        for i in range(len(nums)-2):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            s=i+1
            e=len(nums)-1
            while(s<e):
                if nums[i]+nums[s]+nums[e]==0:
                    l.append([nums[i], nums[s], nums[e]])
                if nums[i]+nums[s]+nums[e]<0:
                    curr_s=s
                    while(nums[curr_s]==nums[s] and s<e):
                        s=s+1
                else:
                    curr_e=e
                    while(nums[curr_e]==nums[e] and s<e):
                        e=e-1
        return l
        
