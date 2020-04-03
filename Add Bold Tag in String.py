class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """

        start = -1
        end = -1
        ans = ''
        for i, c in enumerate(s):
            tmp_end = 0
            #for each word in dict, see if it occurs in s[1:] and get max length word that satisfy the condition
            for d in dict:
                if s[i:].startswith(d):
                    tmp_end = max(tmp_end, len(d))
            if tmp_end!=0:
                if start==-1:
                    start=i
                end = max(end, tmp_end+i)
                continue
            if i>=end and start!=end:
                ans+="<b>"+s[start:end]+"/<b>"
                start = -1
                end = -1
            if start==-1:
                ans+=c
        
        if start>-1:
            ans+="<b>"+s[start:end]+"</b>"
        return ans
        
ob = Solution()
s = "aaabbcc"
dict = ["aaa","aab","bc"]
ans = ob.addBoldTag(s, dict)
print(ans)
