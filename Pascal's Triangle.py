class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        each = []
        for i in range(1, numRows+1):
            li = []
            for j in range(0, i):
                li.append(1)
            each.append(li)
        for j in range(2, len(each)):
            for i in range(1, j):
                if(each[j-1][i-1] and each[j-1][i]):
                    each[j][i] = each[j-1][i-1]+each[j-1][i]
        return each
