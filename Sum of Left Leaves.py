# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.traverse(root)
        return self.ans
        
    def traverse(self, node):
            if node is None:
                return None
            if(node.left is not None and node.left.left is None and node.left.right is None):
                self.ans+=node.left.val
            self.traverse(node.left)
            self.traverse(node.right)
        
        
