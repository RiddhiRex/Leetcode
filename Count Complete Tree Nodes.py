# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.cnt = 0
        def traverse(node):
            if node is None:
                return None
            self.cnt+=1
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return self.cnt
