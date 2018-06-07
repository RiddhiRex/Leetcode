class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        l = []
        for each in range(0,num+1):
            count=0
            while(each):
                if (each&1):
                    count=count+1
                each=each>>1
            l.append(count)
        return l
