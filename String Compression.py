class Solution:
    def compress(self, chars: List[str]) -> int:

        if not chars:
            return 0
        
        # Initialize pointers
        write_idx = 0
        read_idx = 0
        
        while read_idx < len(chars):
            char = chars[read_idx]
            count = 0
            
            # Count consecutive repetitions of current character
            while read_idx < len(chars) and chars[read_idx] == char:
                read_idx += 1
                count += 1
            
            # Write compressed character and count
            chars[write_idx] = char
            write_idx += 1
            if count > 1:
                for digit in str(count):
                    chars[write_idx] = digit
                    write_idx += 1
        
        return write_idx

            
 #solution2
class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        idx=1
        i=1
        while(i<len(chars)):
            cnt=1
            while(chars[i-1]==chars[i]):
                cnt+=1
                if(i+1==len(chars)):
                    break
                i+=1
            if(cnt)>1:
                for k in str(cnt):
                        chars[idx]=k
                        idx+=1

            chars[idx] = chars[i]
            idx+=1
            i+=1
        
        return idx
                
            
            
