import string
class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        status = ""
        if "." in IP:
            part = IP.split(".")
            if(len(part)!=4):
                return "Neither"
            for i in range(len(part)):
                if not part[i].isdigit() or int(part[i])<0 or int(part[i])>255 or (part[i][0]=="0" and len(part[i])>1):
                    return "Neither"
            return "IPv4"
        if ":" in IP:
            part = IP.split(":")
            if(len(part)!=8):
                return "Neither"
            for i in range(len(part)):
                if len(part[i])>4 or len(part[i])<1 or not all(c in string.hexdigits for c in part[i]):
                    return "Neither"
            return "IPv6"
        return "Neither"
