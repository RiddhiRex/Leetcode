'''
Given an array of integers greater than zero, find if it is possible to split it in two subarrays
(without reordering the elements), such that the sum of the two subarrays is the same. 
Print the two subarrays.
'''

def findSplitPoint(arr) : 
    left_sum=0
    for no in arr:
        left_sum+=no
        
    right_sum=0
    for i in range(len(arr)-1, -1, -1):
        right_sum+=arr[i]
        left_sum-=arr[i]
        if right_sum==left_sum:
            return i
    return -1
arr = [1,2,3,4,5,5]
split_idx = findSplitPoint(arr)
print(split_idx)
if split_idx!=-1:
    print(arr[0:split_idx], arr[split_idx:])
