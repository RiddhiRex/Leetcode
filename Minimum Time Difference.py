class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        m=[]
        time = []
        for each in timePoints:
            if(each[:2]=='00'):
                m.append((24*60) + int(each[3:]))
            else:
                m.append((int(each[:2])*60) + int(each[3:]))
            
        m = sorted(m) 
        print(m)
        for i in range(len(m)):
            if(i==len(m)-1):
                time.append((m[0]+(24*60))-m[i])
            else:
                time.append((m[i+1]-m[i]))
        print(time)
        return min(time)
    
