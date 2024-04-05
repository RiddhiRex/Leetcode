"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = []
        free_time = []
        for sch in schedule:
            for s in sch:
                intervals.append([s.start, s.end])
        print(intervals)
        intervals = sorted(intervals)
        prev_end = intervals[0][-1]
        for start, end in intervals[1:]:
            if start>prev_end:
                free_time.append(Interval(prev_end, start))
            prev_end = max(prev_end, end)
        return free_time
