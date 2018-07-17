# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head==None or head.next == None):
            return head
        even = head.next
        evenhead = head.next
        odd = head
        while(even!=None and even.next!=None):
            odd.next=odd.next.next
            odd =odd.next
            even.next = even.next.next
            even = even.next
        odd.next = evenhead
        return head
                
                
            
            
