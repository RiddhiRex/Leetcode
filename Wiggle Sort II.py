class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        mid = (len(nums)+1) //2
        l = nums[0:mid]
        r = nums[mid:]
        nums[0::2] = l[::-1]
        nums[1::2] = r[::-1]
