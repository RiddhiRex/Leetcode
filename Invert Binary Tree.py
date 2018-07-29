# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def traverse(node):
            if node is None:
                return None
            temp = node.left
            node.left = node.right
            node.right = temp
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return root
        
