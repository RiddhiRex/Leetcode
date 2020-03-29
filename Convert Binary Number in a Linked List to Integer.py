# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        node=head
        no=""
        while(node!=None):
            no=no+str(node.val)
            node=node.next
        return int(no, 2)
        
