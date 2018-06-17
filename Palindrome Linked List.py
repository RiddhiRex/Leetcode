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
            
        
