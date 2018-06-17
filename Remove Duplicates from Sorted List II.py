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
