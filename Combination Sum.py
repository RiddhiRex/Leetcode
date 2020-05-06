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

        
