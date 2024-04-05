solution 1:
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        def dfs(nums, trgt, idx, cur_list, total):
            if total==trgt:
                if cur_list not in self.ans:
                    self.ans.append(cur_list)
            if total>trgt:
                return
            for i in range(idx, len(nums)):
                if i==idx or nums[i-1]!=nums[i]:
                    dfs(nums, trgt, i+1, cur_list+[nums[i]], total+nums[i])
            return
        
        candidates = sorted(candidates)
        dfs(candidates, target, 0, [], 0)
        return self.ans

        
        
solution 2:
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        for i in range(1, len(candidates)+1):
            l = itertools.combinations(candidates, i)
            for j in l:
                if sum(j)==target and sorted(j) not in ans:
                    ans.append(sorted(j))
        return ans
        
solution 3:
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums, trgt, idx, ans, path):
            if trgt==0:
                if path not in ans:
                    ans.append(path)
                return
            if trgt<0:
                return
            for i in range(idx, len(candidates)):
                dfs(nums, trgt-nums[i], i+1, ans, path+[nums[i]])
            return
                
        candidates.sort()
        ans = []
        dfs(candidates, target, 0, ans, [])
        return ans
        
