# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = l1
        n1 =""
        dummy =ListNode(-1)
        newcurr =dummy
        if(l1 is None and l2 is None):
            return 0
        elif(l1 is None):
            n1=0
        elif(l2 is None):
            n2=0
        while(curr is not None):
            n1=n1+str(curr.val)
            #n1 = n1+curr.val        
            curr = curr.next
        n2=""

        curr = l2
        while(curr is not None):
            n2=n2+str(curr.val)
            curr= curr.next
        print(n1, n2)
        sum = int(n1)+int(n2)
        print(sum)
        if(sum==0):
            dummy.next =ListNode(sum)
            return dummy.next
        while(sum>0):
            n = sum%10
            newcurr.next = ListNode(n)
            newcurr = newcurr.next
            sum = sum//10
        newcurr.next = None
        return dummy.next
            
            
        
            
        
