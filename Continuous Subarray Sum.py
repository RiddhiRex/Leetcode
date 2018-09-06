class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        summ=0
        dic={}
        dic = {0 : -1}
        for i, no in enumerate(nums):
            summ=summ+no
            if(k):
                summ = summ%k
            
            if summ in dic.keys():
                if(i-dic[summ] > 1):  
                    return True
            else:
                dic[summ]=i
        return False
