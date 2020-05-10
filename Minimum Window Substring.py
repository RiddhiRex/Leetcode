class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ds = collections.defaultdict(int)
        dt = collections.defaultdict(int)
        start = 0
        shortest_len = float("inf")
        shortest_start_idx = 0
        length = 0
        for i in t:
            dt[i]+=1
        i=0
        while(i<len(s)):
            ds[s[i]]+=1
            
            if ds[s[i]]<=dt[s[i]]:
                length+=1
                
            if length==len(t):
                while(ds[s[start]]>dt[s[start]] or dt[s[start]]==0):
                    ds[s[start]]-=1
                    start+=1
                if i-start+1<shortest_len:
                    shortest_len=i-start+1
                    shortest_start_idx = start
                    
            i+=1
            
        if shortest_len==float("inf"):
            return ""
        return s[shortest_start_idx:shortest_start_idx+shortest_len]
