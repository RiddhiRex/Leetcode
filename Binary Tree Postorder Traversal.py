# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.l = []
        self.traverse(root)
        return self.l
    
    def traverse(self, root):    
        if root is None:
            return None
        self.traverse(root.left)
        self.traverse(root.right)
        self.l.append(root.val)
        
        
