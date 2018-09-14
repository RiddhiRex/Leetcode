class Solution(object):

    def IPValidate(self, IP):
        parts = IP.split(".")
        if(len(parts)!=4):
            return False
        for i in range(len(parts)):
            if not parts[i].isdigit() or int(parts[i])<0 or int(parts[i])>255 or (parts[i][0]=="0" and len(parts[i])>1):
                return False
        return True
    
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        cnt=0
        ans =[]
        self.listIp=[]
        if(len(s)==0):
            return []
        self.generateIP("", s)
        for each in self.listIp:
            if self.IPValidate(each) is True:
                ans.append(each)
        return ans
        
    def generateIP(self, ip, remaining_st):
        if(len(remaining_st)==0):
            self.listIp.append(ip)
            return
          
        if(len(remaining_st)==1):
            self.generateIP(ip+(remaining_st[0]), remaining_st[1:])
        else:
            self.generateIP(ip+(remaining_st[0]+"."), remaining_st[1:])
            
        if(len(remaining_st)==2):
            self.generateIP(ip+(remaining_st[0:2]), remaining_st[2:])
        else:
            self.generateIP(ip+(remaining_st[0:2]+"."), remaining_st[2:])
            
        if(len(remaining_st)==3):
            self.generateIP(ip+(remaining_st[0:3]), remaining_st[3:])
        else:
            self.generateIP(ip+(remaining_st[0:3]+"."), remaining_st[3:])   
        return
