class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        no = "1"
        i=0
        while(n>1):
            st=""
            i=0
            while(i <len(no)):
                l = no[i]
                count=0
                while i<len(no) and l==no[i]:
                    i=i+1
                    count =count+1
                st=st+str(count)+str(l)
            print(st)
            no = st
            n=n-1
        return no
            
            
            
             
