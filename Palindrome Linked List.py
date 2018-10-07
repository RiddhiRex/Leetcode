# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curr = head
        l = []
        while(curr is not None):
            l.append(curr.val)
            curr= curr.next
        rev = l[::-1]
        if(l[:len(l)//2]==rev[:len(l)//2]):
            return True
        else:
            return False
            
#Solution 2 with no extra space       
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        dummy=ListNode(0)
        dummy.next = head
        curr=head
        prev = dummy
        fast=head
        if(head is None or head.next is None):
            return True
        while(fast is not None and fast.next is not None):
            fast=fast.next.next
            nxt = curr.next
            curr.next = prev
            prev= curr
            curr= nxt

        if fast is None:
            #even elements in lists
            h1=prev
            h2=curr
        elif fast is not None and fast.next is None:
            #move the header for odd elements in list
            h1=prev
            h2=curr.next
        
        while(h1 is not None and h2 is not None):
            print(h1.val, h2.val)
            if h1.val==h2.val:
                h1=h1.next
                h2=h2.next
            else:
                return False
        
        return True
