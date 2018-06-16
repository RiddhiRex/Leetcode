# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        curr=head
        while(curr is not None):
            if curr.val==val:
                if(curr==head):
                    if(curr.next is not None):
                        head=curr.next
                    else:
                        return []
                else:
                    prev.next=curr.next
            else:
                prev=curr
            curr = curr.next
        return head
                
        
        
