#Using the logic from https://www.youtube.com/watch?v=EHpS2TBfWQg
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        cur1 = head
        cur2= Node(head.val)
        cur2.next = None
        cur2.random = cur1
        head2= cur2
        next = {}
        while(cur1.next is not None):
            cur2.next = Node(cur1.next.val)
            cur2.next.random = cur1.next
            cur2 = cur2.next
            cur1 = cur1.next
        cur2.next = None

        cur1 = head
        cur2 = head2
        while(cur1 is not None):
            next[cur1]=cur1.next
            cur1.next = cur2
            cur1 = next[cur1]
            cur2 = cur2.next

        cur1 = head
        cur2 = head2           
        while(cur2 is not None):
            if cur2.random is not None and cur2.random.random is not None:
                cur2.random = cur2.random.random.next
            else:
                cur2.random = None
            cur2 = cur2.next

        while(cur1 is not None):
            cur1.next = next[cur1]
            cur1 = cur1.next
        return head2

        




            
            


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return head

        curr1=head
        head2=RandomListNode(head.label)
        curr2=ListNode(-1)
        curr2=head2
        curr2.next=None
        copies = {}
        while(curr1.next is not None):
            t = RandomListNode(curr1.next.label)
            curr2.next=t
            copies[curr1]=curr1.next
            curr1=curr1.next
            curr2=curr2.next
        curr2.next=None
        curr1=head
        curr2=head2
        while(curr1 is not None):
            curr2.random = curr1
            c_nxt = curr1.next
            curr1.next = curr2
            curr1 =c_nxt
            curr2 = curr2.next
        curr1=head
        curr2=head2
        while(curr2 is not None):
            if(curr2.random is not None and curr2.random.random is not None):
                curr2.random=curr2.random.random.next
            else:
                curr2.random=None
            curr2=curr2.next
        curr1=head
        while(curr1 is not None):
            if curr1 in copies.keys():
                curr1.next = copies[curr1]
            else:
                curr1.next=None
            curr1=curr1.next
        return head2
            
        
        
            
            
