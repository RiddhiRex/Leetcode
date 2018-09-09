import collections
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        st = collections.Counter(S)
        if any(v >(len(S)+1)/2 for k,v in st.items()):
            return ""
        
        ans ="*"
        while(st):
            for item, cnt in st.most_common():
                if ans[-1]!=item:
                    ans=ans+item
                    st[item]-=1
                    if(st[item]==0):
                        del st[item]
                    break
        return ans[1:]
