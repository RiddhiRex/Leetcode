'''
# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
'''
class Solution:
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """

        if head==None:
            head = Node(insertVal, None)
            head.next=head
            return head
        prev = head
        cur = head.next
        while(cur!=head):
            if prev.val<=insertVal and cur.val>=insertVal:
                break
            if prev.val>cur.val and (prev.val<=insertVal or cur.val>=insertVal):
                break
            prev = cur
            cur=cur.next
            
        prev.next = Node(insertVal, cur)
        return head
        
