class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
            result = 0
            while n:
                print(bin(result), bin(n))
                result ^= n
                n >>= 1
                print(bin(result), bin(n))
                print("=------=")
            return result
