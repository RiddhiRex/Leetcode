class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)[2:][::-1]
        padding = 32-len(b)
        no = b+"0"*padding
        return int(no, 2)
        
