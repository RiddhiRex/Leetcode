class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nos = sorted(set(nums))
        if len(nos)<3:
            return nos[-1]
        else:
            return nos[len(nos)-3]
        
