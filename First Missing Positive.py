class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        #Put respective numbers in respective places like number 1 in first position
        while(i<len(nums)):
            if nums[i]>0 and nums[i]-1<len(nums) and nums[i]!=nums[nums[i]-1]:
                tmp = nums[nums[i]-1]
                nums[nums[i]-1]= nums[i]
                nums[i] = tmp
            else:
                i+=1
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1
                
    
        
            
            
        
