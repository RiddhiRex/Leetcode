import itertools 
class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l = []
        if(len(s)%2!=0):
            mid = None
            cnt = collections.Counter(s)
            for k, v in cnt.iteritems():
                if(v%2!=0):
                    if(mid is None):
                        mid = k
                    else:
                        return [] 
        perm = set(itertools.permutations(s, len(s)))
        for each in perm:
            if(len(s)%2!=0) and (each[len(each)//2]!=mid):
                continue
            st = "".join(each)
            if (st == st[::-1]):
                l.append(st)
        return l
        
