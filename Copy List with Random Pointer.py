#Using the logic from https://www.youtube.com/watch?v=EHpS2TBfWQg
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

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
            
        
        
            
            
