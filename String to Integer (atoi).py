class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip(" ")
        if(len(str)==0 or (str[0].isdigit() is False and str[0]!="-" and str[0]!="+")):
            return 0
        if(any(c.isdigit() for c in str) is False):
            return 0
        i=0
        num =""
        sign="+"
        while(str[i].isdigit() is False):
            if(str[i]=="-"):
                sign="-"
            if(i==1):
                return 0
            i=i+1
        while(i<len(str) and (str[i].isdigit() is True)):
            if(str[i]!="+"):
                num=num+str[i]
            i=i+1
        print(num)
        if(sign=="-"):
            print(num)
            num = -int(num)    
        else:
            print(num)
            num=int(num)
        if(num<=-2**31):
            return (-2**31)
        elif(num>=2**31):
            return (2**31)-1
        else:
            return num
        
