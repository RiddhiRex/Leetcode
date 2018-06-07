class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        no=0
        l=[]
        for each in digits:
            no=no+each
            no= no*10
        no = (int(no//10))+1

        while(no>0):
            l.append(no%10)
            no=no//10

        return l[::-1]
