class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        numlog = []
        wrdlog = []
        for log in logs:
            wrd = log.split(" ")
            if wrd[1].isdigit() == True:
                numlog.append(log)
            else:
                wrdlog.append((" ".join(wrd[1:]), wrd[0]))
        wrdlog.sort()
        ans = [wrd[1]+" "+wrd[0] for wrd in wrdlog]+numlog
        return ans
        
