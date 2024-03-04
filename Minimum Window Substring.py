class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if (len(s)==0  or len(t)==0):
            return ""
        required_char_dict = collections.Counter(t)
        formed_char_dict = collections.defaultdict(int)
        left = right = 0
        min_len = float("inf")
        start_idx = 0
        end_idx = len(s)-1
        req_chars = len(required_char_dict)
        char = 0
        
        while(right <len(s)):
            if s[right] in required_char_dict.keys():
                formed_char_dict[s[right]]+=1
                if(formed_char_dict[s[right]]==required_char_dict[s[right]]):
                    req_chars -=1
                
            while(req_chars == 0):
                if(right-left+1 <min_len):
                    min_len=right-left+1
                    start_idx=left
                    
                if (s[left] in required_char_dict):
                    formed_char_dict[s[left]]-=1
                    if(formed_char_dict[s[left]]<required_char_dict[s[left]]):
                        req_chars +=1
                    
                
                left+=1
            right+=1
        if(min_len==float("inf")):
            return ""
        else:
            return s[start_idx:start_idx+min_len]
                    
                
            
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
