class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = len(nums)
        i = 0
        while(i<j):
            if nums[i]==val:
                nums[i]=nums[j-1]
                j-=1
            else:
                i+=1
        return j
    
