class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i=0
        j=-1
        s=s.lower()
        for each in s:
            if each in string.punctuation:
                s= s.replace(each,"")
            if each ==' ':
                s= s.replace(each,"")
        while(i<len(s)/2):
            if not s[i]==s[j]:
                return False
            else:
                i+=1
                j-=1
        return True

#solution 2
import string
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i=0
        s=s.lower()
        while(i<len(s)):
            if s[i] in string.punctuation or s[i]==" ":
                s = s[0:i]+s[i+1:]
            else:
                i+=1
        return s==s[::-1]
