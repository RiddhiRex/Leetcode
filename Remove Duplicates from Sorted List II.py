# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        cur = head
        while(cur is not None):
            while(cur.next is not None and cur.val == cur.next.val):
                cur = cur.next
            if prev.next != cur:
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        return dummy.next
        

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head is None):
            return head
        dummy=ListNode(-1)
        dummy.next=head
        prev = dummy
        curr=head
        while(curr.next is not None):
            if(curr.val!=curr.next.val):
                prev=curr
                print("here", curr.val)
                
            else:
                while(curr.next is not None) and (curr.val==curr.next.val):
                    curr=curr.next
                prev.next = curr.next
            curr=curr.next
            if(curr is None):
                break
        return dummy.next
