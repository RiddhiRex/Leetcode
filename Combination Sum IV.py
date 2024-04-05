class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1 #only 1 way to get 0 as target sum: by not choosign any number
        
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[target]


Solution 2:
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res_list = []
        def calculate(nums, cur_list, total):
            if total==target:
                l = itertools.permutations(cur_list)
                for each in set(l):
                    res_list.append(each)
                return
            if total>target:
                return
            for i in range(len(nums)):
                calculate(nums[i:], cur_list+[nums[i]], total+nums[i])
            return
                           
                           
        calculate(nums, [], 0)
        print(res_list)
        return len(res_list)

