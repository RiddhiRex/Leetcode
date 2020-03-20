class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1)
        l2 = len(num2)
        if l1>l2:
                num1 = list(num1)
                num2 = ['0']*(l1-l2)+list(num2)
        else:
                num1=['0']*(l2-l1)+list(num1)
                num2 = list(num2)
         
        r = 0
        sum=[0]*(max(l1, l2)+1)
        for i in range(max(l1,l2)-1, -1, -1):
            cur_sum = int(num1[i])+int(num2[i])+r
            if cur_sum>=10:
                sum[i+1]=str(cur_sum%10)
                r = cur_sum//10
            else:
                sum[i+1]= str(cur_sum)
                r = 0
        if r!=0:
            sum[0]=str(r)
            sum="".join(sum)
        else:
            sum="".join(sum[1:])
        return sum
            
                
