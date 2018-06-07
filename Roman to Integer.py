class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        dict["I"]=1
        dict["V"]=5
        dict["X"]=10
        dict["L"]=50
        dict["C"]=100
        dict["D"]=500
        dict["M"]=1000
        prev=0
        cnt =0
        sum=0
        wrong =["IIII", "VVVV","XXXX","LLLL","CCCC","DDDD","MMMM","IXI","IVI","IIV","IIX","ILI","ICI","IDI", "IMI"]
        for each in wrong:
            if(s.find(each)!=-1):
                return False
        for each in s:
            if each not in dict:
                print(False)
            if(dict[each] <= sum and dict[each]<=prev):
                sum=sum+dict[each]
            elif(dict[each]>sum):
                sum = dict[each]-sum
            elif(dict[each]>prev):
                sum = sum+dict[each]-prev-prev
            prev = dict[each]

        return sum                
            
