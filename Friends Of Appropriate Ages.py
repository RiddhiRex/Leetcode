class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ans = 0
        cnt = collections.Counter(ages)
        for age1, cnt1 in cnt.items():
            for age2, cnt2 in cnt.items():
                if (age2<=0.5*age1+7 or age2>age1 or (age2>100 and age1<100)):
                    continue
                ans += cnt1*cnt2
                if age1==age2:
                    ans-=cnt1
        return ans
        
