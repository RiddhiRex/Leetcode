# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head is None):
            return []
        elif(head.next is None):
            return head
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        curr1 = head.next
        curr2 = head
        curr1loc =1
        t =head
        while(curr1 is not None):
            prev = dummy
            curr2 = dummy.next
            curr2loc =0
            c1 = curr1
            cn1 =curr1.next 
            c1loc=curr1loc
            c2loc=curr2loc
            t = dummy.next
            while(c2loc+1<c1loc):
                t= t.next
                c2loc=c2loc+1
            while(curr2loc<curr1loc):
                c2 = curr2
                if(curr1.val < curr2.val):
                    prev.next = c1
                    t.next = cn1
                    c1.next = c2
                    break
                curr2 = curr2.next
                prev = prev.next
                curr2loc = curr2loc+1
            curr1loc= curr1loc+1
            curr1 = cn1
        
        return dummy.next
                    
        
        
        
