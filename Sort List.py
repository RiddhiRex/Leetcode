# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        prev=None
        slow=head
        fast=head
        while(fast is not None and fast.next is not None):
            prev = slow
            slow=slow.next
            fast=fast.next.next
        prev.next=None
        l1=self.sortList(head)
        l2=self.sortList(slow)
        
        return self.mergeList(l1, l2)
    
    def mergeList(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        dummy=ListNode(0)
        curr=dummy
        while(l1 is not None and l2 is not None):
            if l1.val<l2.val:
                curr.next=l1
                l1=l1.next
                curr=curr.next
            else:
                curr.next=l2
                l2=l2.next
                curr=curr.next
        if l1 is not None:
            curr.next=l1
        if l2 is not None:
            curr.next=l2
        return dummy.next
        
