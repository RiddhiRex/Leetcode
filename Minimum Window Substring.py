class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dt=collections.defaultdict(int)
        ds=collections.defaultdict(int)
        start=0
        cnt=0
        short_start=0
        shortest=float("inf")
        i=0
        for each in t:
            dt[each]+=1
            
        while(i<len(s)):
            ds[s[i]]+=1
            
            if ds[s[i]]<=dt[s[i]]:
                cnt+=1
                
            if cnt==len(t):
                while(ds[s[start]]>dt[s[start]] or dt[s[start]]==0):
                    ds[s[start]]-=1
                    start=start+1
                    
                if i-start+1<=shortest:
                    shortest = i-start+1
                    short_start=start 
            i+=1
        if shortest==float("inf"):
            return ""
        return s[short_start:short_start+shortest]
   
