class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = collections.Counter(nums)
        l = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
        max_occurance = l[0][1]
        print(max_occurance, l[0][0])
        nos = []
        for k, v in d.items():
            if v==max_occurance:
                nos.append(k)
        min_len=len(nums)
        for no in nos:         
            p = len(nums[nums.index(no):len(nums)-nums[::-1].index(no)])
            min_len = min(min_len, p)
        return min_len
        
