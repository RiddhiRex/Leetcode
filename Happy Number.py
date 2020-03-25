class Solution:
    def isHappy(self, n: int) -> bool:
        no = n
        sum = 0
        l =[no]
        while(sum!=1):
            sum = 0
            num = list(str(no))
            for n in num:
                sum+=int(n)*int(n)
            if sum==1:
                return True
            no = sum
            if sum not in l:
                l.append(sum)
            else:
                return False
        return True
            
