import collections
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        st = collections.Counter(s)
        keys = sorted(st, key=st.get, reverse=True)
        for k in keys:
            k = k*st[k]
            ans=ans+k
        return ans
                
        
