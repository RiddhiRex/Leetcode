class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        ans = ""
        i=0
        while(i<len(chars)-1):
            if chars[i]==chars[i+1]:
                cnt=1
                while(i+1<len(chars) and chars[i]==chars[i+1]):
                        if(i+2<len(chars)):
                            chars= chars[0:i+1]+chars[i+2:]
                        else:
                            chars= chars[0:i+1]
                        cnt+=1
                cnt=str(cnt)
                while(len(cnt)>0):
                    chars.insert(i+1, cnt[-1])
                    cnt=cnt[:-1]
            i=i+1
        return len(chars)
                
        
