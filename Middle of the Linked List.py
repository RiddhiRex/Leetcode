# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head.next is None):
            return head
        cur1= head
        cur2=head
        while(cur2 is not None and cur2.next is not None):
            cur1=cur1.next
            cur2=cur2.next.next

        return cur1
