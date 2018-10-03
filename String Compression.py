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
