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

            
        
