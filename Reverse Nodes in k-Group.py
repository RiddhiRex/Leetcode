# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return
        dummy = ListNode(-1)
        dummy.next=head
        prev= dummy
        curr=head
        i=k
        while(curr is not None):

            end = prev
            start = curr
            check=curr
            i=1
            while(check is not None and i<k):
                check=check.next
                i+=1
            if(i!=k or check is None):
                return dummy.next
            i=0
            while(i<k and curr is not None):
                cnext = curr.next
                curr.next = prev
                prev=curr
                curr=cnext
                i+=1
            if curr is not None:
                print(prev.val, curr.val)
            start.next = curr
            end.next = prev
            prev= start
        return dummy.next
            
            
                
            
            
