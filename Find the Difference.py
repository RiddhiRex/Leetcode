class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dict ={}
        for each in s:
            if each in dict.keys():
                dict[each]=dict[each]+1
            else:
                dict[each]=1
        for each in t:
            if each in dict.keys():
                dict[each]=dict[each]-1
            else:
                print each
                return each
        for k, v in dict.iteritems():
            if v!=0:
                print k
                return k

solution2:
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ans=""
        for each in s:
            if each in t:
                t = t.replace(each, "", 1)
            else:
                ans=ans+each
        ans=ans+t
        return ans
        
