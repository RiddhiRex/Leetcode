class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        wrd = []
        wrd= s.split()
        rev=[]

        for each in wrd:
            rev.append(each[::-1])
        return ' '.join(rev)
