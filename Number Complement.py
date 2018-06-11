class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        l=""
        while(num):
            if(num&1):
                l=l+"0"
            else:
                l=l+"1"
            num=num>>1
        no = int((l)[::-1], 2)
        return (int(no))
