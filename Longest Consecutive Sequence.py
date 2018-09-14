class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lookup = {}
        ans = 0
        for each in nums:
            lookup[each]=each
        for each in nums:
            if each-1 in lookup:
                continue
            cnt=1
            i=1
            while(each+i in lookup):
                cnt+=1
                i+=1
            ans=max(ans, cnt)
        return ans
            
