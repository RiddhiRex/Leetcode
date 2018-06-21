# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if(head is None or head.next is None):
            return None
        f = head.next
        s=head
        while(s is not None and f.next is not None):
            if(s==f):
                break
            s=s.next
            f=f.next.next
        if(s!=f):
            return None
        s =head
        while(s!=f):
            s=s.next
            f=f.next
        return s
        
            
        
