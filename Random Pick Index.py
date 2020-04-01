class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        idxs = []
        for i, no in enumerate(self.nums):
            if no==target:
                idxs.append(i)
        return idxs[random.randint(0, len(idxs)-1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
