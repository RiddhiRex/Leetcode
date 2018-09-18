# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        node=root
        succ=None
        while(node is not None):
            if node.val>p.val:
                succ=node
                node=node.left
            else:
                node=node.right
        return succ
