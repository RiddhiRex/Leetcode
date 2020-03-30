'''
Strobogrammatic Number
======================
A strobogrammatic number is a number that looks the same when rotated 180
degrees (looked at upside down).
Write a function to determine if a number is strobogrammatic. The number is
represented as a string.
For example, the numbers "69", "88", and "818" are all strobogrammatic.
'''
class Solution(object):
    def isStrobogrammatic(self, num):
        d = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        st_num=""
        for no  in num:
            if no not in d:
                return False
            st_num +=d[no]
        print(st_num)
        if int(st_num[::-1])==int(num):
            return True
        else:
            return False

s = Solution()
print(s.isStrobogrammatic('96'))
