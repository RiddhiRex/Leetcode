class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = collections.defaultdict(list)
        for i, each in enumerate(nums):
            if each not in d:
                d[each].append(i)
            else:
                for v in d[each]:
                    if abs(i-v)<=k:
                        return True
                d[each].append(i)
        return False
        
        
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic={}
        for i in range(len(nums)):
            if nums[i] in dic.keys() and abs(dic[nums[i]]-i)<=k:
                return True
            else:
                dic[nums[i]]=i
        return False
    
