
class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        readbuf = [None]*4 
        write_idx = 0
        EOF = False 
        while(write_idx<n and EOF!=True)
            charcnt = read4(readbuf)
            if charcnt<4:
                EOF=True
                
            for i in range(len(charcnt)):
                buf[write_idx]=readbuf[i]
                write_idx+=1 
            
                if write_idx==n:
                    return write_idx
        return write_idx
