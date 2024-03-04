class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        def calculate(nums, cur_list, total):
            if total==target:
                self.ans.append(cur_list)
            elif total>target:
                return
            for i in range(len(nums)):
                calculate(nums[i:], cur_list+[nums[i]], total+nums[i])
        calculate(candidates, [], 0)
        return self.ans
        
        
        

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def combinationSumRecurse(candidates, start, path, ans, tmptarget):
            if tmptarget==0:
                ans.append(list(path))
            while start<len(candidates) and candidates[start]<=tmptarget:
                path.append(candidates[start])
                combinationSumRecurse(candidates, start, path, ans, tmptarget-candidates[start])
                path.pop()
                start+=1
               
        ans = []
        combinationSumRecurse(sorted(candidates), 0, [], ans, target)
        return ans

        
