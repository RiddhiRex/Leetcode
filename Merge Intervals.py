class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = operator.itemgetter(0))
        ans = []
        for s, e in intervals:
            if ans and s<=ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], e)
            else:
                ans.append([s, e])
        return ans
            
        


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start)
        i=1
        lst = []
        print(intervals)
        for interval in intervals:
            if(lst and interval.start <= lst[-1].end):
                lst[-1].end = max(lst[-1].end, interval.end)
            else:
                lst.append(interval)
            i=i+1
        return lst

            
        
