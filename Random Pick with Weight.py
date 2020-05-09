class Solution:
    def __init__(self, w: List[int]):
        self.sum = [0]*len(w)
        for i, no in enumerate(w):
            if i==0:
                self.sum[i]=no
            else:
                self.sum[i]=self.sum[i-1]+no
        print(self.sum)

    def pickIndex(self) -> int:
        val = random.randint(0, self.sum[-1]-1)
        '''
        #Method 1:
        l=0
        r = len(self.sum)-1
        while(l<r):
            mid=(l+r)//2
            if self.sum[mid]<=val:
                l = mid+1
            else:
                r = mid
        return r
        '''
        #Mehtod 2:
        for i in range(len(self.sum)):
            if self.sum[i]>val:
                return i
