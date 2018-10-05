from collections import Counter
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        li = []
        for i in range(0, len(strs)):
            l= []
            for j in range(0, len(strs)):
                if(i==j):
                    continue
                if(len(strs[i])!=len(strs[j])):
                    continue
                if(Counter(strs[i])==Counter(strs[j])):
                        l.append(strs[j])
            l.append(strs[i])              
            if(sorted(l) not in li and len(l)!=0):
                li.append(sorted(l))
            if(len(l)==0 and strs[i] not in li):
                li.append([strs[i]])
               
        return (li)
        
        
        #solution 2:
    class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = []
        i=0
        dic = {}
        for each in strs:
            if "".join(sorted(each)) not in dic:
                dic["".join(sorted(each))]=[each]
            else:
                dic["".join(sorted(each))].append(each)
        return dic.values()
            
                
            
            
