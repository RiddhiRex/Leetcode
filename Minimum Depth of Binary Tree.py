# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root is None):
            return 0
        if(root.left == None):
            return self.minDepth(root.right)+1
        if(root.right == None):
            return self.minDepth(root.left)+1
        return min(self.minDepth(root.right)+1, self.minDepth(root.left)+1)
        
