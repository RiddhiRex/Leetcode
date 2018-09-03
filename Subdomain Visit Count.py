import collections
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        ans = []
        visit=collections.defaultdict(int)
        for d in cpdomains:
            val = d.split(" ")[0]
            site = d.split(" ")[1]
            w=""
            i=len(site)-1
            while(len(w)<len(site)):
                while(i>=0 and site[i]!="." and site[i]!=" "):
                    i=i-1
                if(site[i]==" "):
                    w=site
                else:
                    w=site[i+1:]
                i=i-1
                print(w)
                visit[w]+=int(val)
                
        for k, v in visit.items():
            ans.append(str(v)+" "+k)
        return ans
            
        
