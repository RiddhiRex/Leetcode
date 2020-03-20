class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i=m+n-1
        if(m==0):
            n=n-1
            while(n>=0):
                nums1[n]=nums2[n]
                n=n-1
            return 
        elif(n==0):
            return
        m=m-1
        n=n-1
        while(i>=0):
            if(m>=0 or n>=0):
                if(m>=0 and nums1[m]>nums2[n]):
                    nums1[i]=nums1[m]
                    m=m-1
                elif(n>=0):
                    nums1[i]=nums2[n]
                    n=n-1
                i=i-1
            else:
                break
        return 
            
        
        Solution 2:
   class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        l = m+n-1
        m-=1
        n-=1
        while(m>=0 and n>=0):
            if nums1[m]>nums2[n]:
                nums1[l]= nums1[m]
                m-=1
            else:
                nums1[l]= nums2[n]
                n-=1
            l-=1
        if m>=0:
            nums1[0:l+1]=nums1[0:m+1]
        if n>=0:
            nums1[0:l+1]=nums2[0:n+1]
                
                
