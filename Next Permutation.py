#Logic based on https://www.youtube.com/watch?v=t_TMt_BFGiQ 
    class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        notHighest = False
        for i in reversed(range(len(nums))):
            if nums[i]>nums[i-1]:
                notHighest = True
                break
        d1=i-1
        if notHighest==False:
            nums=sorted(nums)
            return
        
        d2=None
        for j in range(d1+1, len(nums)):

            if nums[j]>nums[d1] and d2 is None:
                d2=j
            elif nums[j]>nums[d1] and (nums[j]-nums[d1])<(nums[d2]-nums[d1]):
                d2=j

        tmp = nums[d1]
        nums[d1]=nums[d2]
        nums[d2]=tmp
        nums[d1+1:]=sorted(nums[d1+1:])
        return 
        
        
                
            
            
                
        
