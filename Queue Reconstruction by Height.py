class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        #Sort by second element
        people.sort(key=lambda x:x[1])
        #Sort in reverse order by first element
        people.sort(key=lambda x:x[0], reverse=True)
        ans = []
        for p in people:
            #insert the p by index in p[i]
            ans.insert(p[1], p)
        return ans
