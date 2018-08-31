class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans = [0]*(len(num1)+len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                ans[i+j]+=(int(num1[i])*int(num2[j]))
                ans[i+j+1]+=ans[i+j]//10
                ans[i+j]=ans[i+j]%10
        st = ""
        for i in range(len(num1)+len(num2)):
            st = st+str(ans[i])

        res = st.rstrip("0")[::-1]
        if res=="":
            return "0"
        else:
            return res
