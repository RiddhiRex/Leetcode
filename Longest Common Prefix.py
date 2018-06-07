class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        success = ""
        if(len(strs)==0):
            return success
        minlen=len(strs[0])
        for each in strs:
            if(len(each)<minlen):
                minlen = len(each)

        for i in range(minlen+1):
            w = strs[0]
            sw = w[:i]
            for each in strs:
                if(each[:i]!=sw):
                    return success
            success = sw
        return success
        
