# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = l1
        newlist = ListNode("")
        newlist.next = None
        prev = newlist
        n= 0
        n2= 0
        while(curr is not None):
            n= n+ curr.val
            curr = curr.next
            if(curr is not None):
                n = n*10
        curr = l2
        while(curr is not None):
            n2= n2+ curr.val
            curr = curr.next
            if(curr is not None):
                n2 = n2*10
      
        n=n+n2
        if(n==0):
            return ListNode(0)
        print(n)
        prev = newlist
        while(n>0):
            m = n%10
            tmp = prev.next
            newnode = ListNode(m)
            prev.next = newnode
            newnode.next = tmp
            n = n/10


        return newlist.next
        
        
        
        
