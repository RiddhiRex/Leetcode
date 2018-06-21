# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        curr = head
        cnt = 0
        G = set(G)
        while(curr is not None):
            if curr.val in G  and (curr.next is not None and curr.next.val not in G or curr.next is None):   
                cnt=cnt+1
            curr = curr.next
        return cnt
            
                
            
