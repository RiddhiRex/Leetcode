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

    
    Solution 2:
    class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        d = collections.Counter(S)
        l = len(S)
        if l%2==0:
            limit=l/2
        else:
            limit=(l/2)+1
        for k,v in d.items():
            if v>limit:
                return ""
            
        d = sorted(d.items(), key=operator.itemgetter(1))
        ans =[None]*l
        a= []
        for k, v in d:
            a.append(k*v)
        a ="".join(a)
        ans[0::2] = a[l/2:]
        ans[1::2] = a[:l/2]
        return "".join(ans)
