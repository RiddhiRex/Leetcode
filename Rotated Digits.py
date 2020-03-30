class Solution:
    def rotatedDigits(self, N: int) -> int:
        def checkno(num):
            nos = str(num)
            valid_nos = "2569"
            not_valid_nos = "347"
            flag = False
            for no in nos:
                if no in valid_nos:
                    flag = True
                elif no in not_valid_nos:
                    return False
            return flag
        
        
        ans = 0
        for i in range(1, N+1):
            if checkno(i)==True:
                ans +=1
        return ans
    
