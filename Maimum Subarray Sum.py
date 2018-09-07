class solution:
#Kadane’s Algorithm(DP):Takes O(n)
   def maxSubarraySum(self, a):
    max_ends_here=0
    max_so_far=0
    for i in range(len(a)):
        max_ends_here=max_ends_here+a[i]
        if(max_so_far<max_ends_here):
            max_so_far=max_ends_here
    return max_so_far
