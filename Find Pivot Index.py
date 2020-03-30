Solution 1:
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = [0 for i in range(len(nums))]
        right_sum = [0 for i in range(len(nums))]
        for i in range(1, len(nums)):
            left_sum[i]=left_sum[i-1]+nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            right_sum[i]=right_sum[i+1]+nums[i+1]
        print(left_sum, right_sum)  
        for i in range(len(nums)):
            if left_sum[i]==right_sum[i]:
                return i
        return -1
            
 Solution 2:
 class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        total = sum(nums)
        for i in range(0, len(nums)):
            if total-nums[i]-left_sum==left_sum:
                return i
            left_sum +=nums[i]
        return -1
