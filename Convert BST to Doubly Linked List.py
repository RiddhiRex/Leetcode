"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def traverse(root):
            head = root
            tail = root
            if root.left:
                left_head, left_tail = traverse(root.left)
                left_tail.right = root
                root.left = left_tail
                head = left_head
                
            if root.right:
                right_head, right_tail = traverse(root.right)
                right_head.left =root
                root.right = right_head
                tail = right_tail
                
            head.left = tail
            tail.right = head
            return head, tail
        
        if root==None:
            return None
        head, tail = traverse(root)
        return head
