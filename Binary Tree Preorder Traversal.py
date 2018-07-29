# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.l = []
        def traverse(node):
            if node is None:
                return None
            self.l.append(node.val)
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return self.l
        
