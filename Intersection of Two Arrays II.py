class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
            dic1 =collections.Counter(nums1)
            ans =[]
            for no in nums2:
                if no in dic1 and dic1[no]>0:
                    ans.append(no)
                    dic1[no]-=1
            return ans
                    
