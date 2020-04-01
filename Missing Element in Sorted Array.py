'''
Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.

Example 1: Input: A = [4,7,9,10], K = 1 Output: 5 Explanation: The first missing number is 5.

Example 2: Input: A = [4,7,9,10], K = 3 Output: 8 Explanation: The missing numbers are [5,6,8,…], hence the third missing number is 8. Example 3:

Input: A = [1,2,4], K = 3 Output: 6 Explanation: The missing numbers are [3,5,6,7,…], hence the third missing number is 6.

Link:https://strstr.io/Leetcode1060-Missing-Element-in-Sorted-Array/
'''
class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #missing contains accumulated number of numbers missing till that index
        missing = [None]*len(nums)
        missing[0]=0
        for i in range(1, len(nums)):
            missing[i]=nums[i]-nums[i-1]-1+missing[i-1]
        print(missing)
        #Check if missing number comes after the end of the array given
        if k>missing[-1]:
            return nums[-1]+k-missing[-1]
        #Binary search to find where the missing number will go
        l=0
        r=len(nums)-1
        while(l!=r):
            mid = (l+r)//2
            if missing[mid]<k:
                l = mid+1
            else:
                r=mid
        print(l)
        return nums[l-1]+k-missing[l-1]
            
        
        
            
            
            
