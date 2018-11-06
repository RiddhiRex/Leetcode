class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i=0
        cnt=1
        l=len(chars)
        for j in range(1, len(chars)+1):
            if j<l and chars[j]==chars[j-1]:
                cnt+=1
            else:
                chars[i]=chars[j-1]
                i+=1
                if cnt>1:
                    for k in str(cnt):
                        chars[i]=k
                        i+=1
                cnt=1
        return i 
    
 #solution2
class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        idx=1
        i=1
        while(i<len(chars)):
            cnt=1
            while(chars[i-1]==chars[i]):
                cnt+=1
                if(i+1==len(chars)):
                    break
                i+=1
            if(cnt)>1:
                for k in str(cnt):
                        chars[idx]=k
                        idx+=1

            chars[idx] = chars[i]
            idx+=1
            i+=1
        
        return idx
                
            
            
