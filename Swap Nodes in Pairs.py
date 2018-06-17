# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy= ListNode(-1)
        dummy.next = head
        curr= head
        prev= dummy
        while(curr is not None and curr.next is not None):
            n1, n2, n3 = curr, curr.next, curr.next.next
            prev.next =n2
            n2.next = n1
            n1.next = n3
            prev = n1
            curr = n3
            
        return dummy.next
