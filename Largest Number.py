class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        li = []
        m=0
        num=[]
        for each in nums:
            num.append(str(each))
        l = itertools.permutations(num)
        for each in l:
            n = ("".join(each))
            li.append(n)
        print(li)
        return sorted(li)[-1]
        
        
