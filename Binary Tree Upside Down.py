# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverse(self, p, parent):
        if p is None:
            return parent 
        root = self.traverse(p.left, p)
        if parent is not None:
            p.left = parent.right
        else:
            p.left=None
        p.right = parent
        
        return root

        
        
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        return self.traverse(root, None)
