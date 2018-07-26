# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def traverse(node ,l):
            if node is None:
                return None
            traverse(node.left, l)
            l.append(node.val)
            traverse(node.right, l)
            
        if root is None:
            return []
        else:
            l =[]
            traverse(root, l)
            return l
            
