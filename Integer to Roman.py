class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic = {1: "I", 4: "IV", 5: "V", 9: "IX", \
               10: "X", 40: "XL", 50: "L", 90: "XC", \
               100: "C", 400: "CD", 500: "D", 900: "CM", \
               1000: "M"}
        keys = sorted(dic.keys(), reverse=True)
        ans=""
        for each in keys:
            while num/each>0:
                num-=each
                ans+=dic[each]
        return ans
