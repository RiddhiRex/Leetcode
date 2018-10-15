# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import math
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None:
            return None
        
        nodeslist = []
        curr=head
        while(curr is not None):
            nodeslist.append(curr)
            curr=curr.next
        l = len(nodeslist)
        mid = int(math.ceil(l/2))
        for i in range(mid):
            nodeslist[i].next=nodeslist[l-i-1]
            nodeslist[l-i-1].next=nodeslist[i+1]
        nodeslist[mid].next=None
        Reorder List
