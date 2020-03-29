solution 1:

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        for i in range(1, len(candidates)+1):
            l = itertools.combinations(candidates, i)
            for j in l:
                if sum(j)==target and sorted(j) not in ans:
                    ans.append(sorted(j))
        return ans
        
        solution 2:
