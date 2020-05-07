# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def buildBst(st, end):
            if st==end:
                return None
            mid = (end+st)//2
            left = buildBst(st, mid)
            node = TreeNode(self.head.val)
            node.left = left
            self.head=self.head.next
            node.right = buildBst(mid+1, end)
            return node
        
        self.head = head
        cur=self.head
        cnt=0
        if head==None:
            return head
        
        while(cur!=None):
            cur=cur.next
            cnt+=1
        return buildBst(0, cnt)            
            
