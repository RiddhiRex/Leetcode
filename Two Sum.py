class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=[]
        for cnt, no in enumerate(nums):
            n = target-no
            nums[cnt]="n"
            if n in nums:
                l.append(cnt)
                l.append(nums.index(n))
        return l
                
#solution 2:
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=[]
        for i, n in enumerate(nums):
            if n in l:
                return [i, nums.index(target-n)]
            else:
                l.append(target-n)
