class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        i=0
        j=0
        for each in moves:
            if each=='U':
                j-=1
            elif each=='D':
                j+=1
            elif each=='R':
                i+=1
            elif each=='L':
                i-=1
        return (i==0 and j==0)

        
