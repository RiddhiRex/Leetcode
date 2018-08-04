# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if(l1 is None and l2 is None):
            return None
        elif(l1 is None):
            return l2
        elif(l2 is None):
            return l1

        prev = ListNode(-1)
        curr=prev
        while(l1 is not None and l2 is not None):
            if(l1.val<l2.val):
                curr.next = l1
                l1=l1.next
            else:
                curr.next = l2
                l2=l2.next
            curr = curr.next
        if(l1 is not None):
            curr.next = l1
        elif(l2 is not None):
            curr.next = l2
        return prev.next
                

        
