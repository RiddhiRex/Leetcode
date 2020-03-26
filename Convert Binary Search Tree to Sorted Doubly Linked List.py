"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
            
    def traverse(self, root):
        head = root
        tail = root
        if root.left is not None:
            left_head, left_tail = self.traverse(root.left)
            left_tail.right = root
            root.left = left_tail
            head = left_head
            
        if root.right is not None:
            right_head, right_tail = self.traverse(root.right)
            right_head.left = root
            root.right = right_head
            tail = right_tail
            
        head.left = tail
        tail.right = head
        return head, tail
        
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root==None:
            return None
        head, tail = self.traverse(root)
        return head
