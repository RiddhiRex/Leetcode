class Solution:
    def removeNthFromEnd(self, head, n):
        if head:
            dummy = ListNode(0)
            dummy.next = head
            fast = dummy
            slow = dummy
            for _ in range(n + 1):
                fast = fast.next
            while fast:
                fast = fast.next
                slow = slow.next
            slow.next = slow.next.next
            return dummy.next
            

solution 2
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        prev= ListNode(-1) #creating dummy node
        prev.next = head
        curr1 = prev
        curr2= prev
        i = n-1
        if(head.next is None and n==1):
            head=None
            return head
        while(i>=0):
            curr1= curr1.next
            i=i-1
        
        while(curr1.next is not None):
    
            curr2=curr2.next
            curr1=curr1.next
        curr2.next = curr2.next.next
        return prev.next
