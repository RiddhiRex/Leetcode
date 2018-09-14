class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        no=str(num)
        nolen=len(str(num))
        ones = {0: "", 1:"One", 2: "Two", 3: "Three", 4: "Four", \
                  5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
        
        teens=  {0:"Ten", 1: "Eleven", 2: "Twelve", 3: "Thirteen", 4: "Fourteen", \
                  5: "Fifteen", 6: "Sixteen", 7: "Seventeen", 8: "Eighteen", 9: "Nineteen"}
        tens= {0:"", 1:"", 2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", \
                  7: "Seventy", 8: "Eighty", 9: "Ninety"}
        hundreds = {0: "", 1:"One Hundred", 2: "Two Hundred", 3: "Three Hundred", 4: "Four Hundred", \
                  5: "Five Hundred", 6: "Six Hundred", 7: "Seven Hundred", 8: "Eight Hundred", 9: "Nine Hundred"}
        levels = ["", "Thousand", "Million", "Billion"]
        levelcnt=1
        ans=[]
        while(nolen>0):
            print(nolen, no[:nolen+1])
            if no=='0':
                return "Zero"
            else:
                if(nolen)>=2:
                    print("here")
                    if int(no[nolen-2])==1:
                        print("asdasd")
                        for i in teens:
                            if int(no[nolen-1])==i:
                                ans.insert(0, teens[i])
                                break
                    else:
                        print("theree")
                        for i in ones:
                            if int(no[nolen-1])==i and ones[i]!="":
                                ans.insert(0, ones[i])
                                break
                        for i in tens:
                            if int(no[nolen-2])==i and tens[i]!="":
                                ans.insert(0, tens[i])
                                break
                elif(nolen==1):
                    for i in ones:
                        if int(no[nolen-1])==i and ones[i]!="":
                            ans.insert(0, ones[i])
                            break
                if(nolen>=3):
                    for i in hundreds:
                        if int(no[nolen-3])==i and hundreds[i]!="":
                            ans.insert(0, hundreds[i])
                            break
            if(nolen>3):
                if(len(ans)>0):
                    print(ans)
                    for i in levels:
                        if ans[0]==i:
                            ans.pop(0)
                            break
                ans.insert(0, levels[levelcnt])
                levelcnt+=1              
            nolen=nolen-3
            
        return " ".join(ans)
