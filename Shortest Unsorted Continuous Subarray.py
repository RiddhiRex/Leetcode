class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        snums = sorted(nums)
        i=0
        j=len(nums)-1
        while(i<len(nums) and snums[i]==nums[i]):
            i+=1
        while(j>i and snums[j] == nums[j]):
            j-=1
        if j-1<0:
            return 0
        else:
            return j-i+1
