class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        monotonic = None
        nos = A
        for i in range(1, len(nos)):
            print(nos[i], nos[i-1])
            if monotonic == None:
                if nos[i]<nos[i-1]:
                    #decreasing order
                    monotonic = 1
                elif nos[i]>nos[i-1]:
                    #increasing order
                    monotonic = 0
            elif monotonic == 1 and nos[i]>nos[i-1]:
                return False
            elif monotonic == 0 and nos[i]<nos[i-1]:
                return False
            else:
                continue

        return True
                
                
