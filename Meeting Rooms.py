# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        start=[]
        end=[]
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()
        
        s=0
        e=0
        room=0
        while(s<len(start)):
            if(start[s]<end[e]):
                room=room+1
                if(room>1):
                    return False
                s=s+1
            else:
                room=room-1
                e=e+1
        return True
            
