# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def checkLeaf(node, l):
            if node.left is None and node.right is None:
                l.append(node.val)
            if(node.left is not None):
                checkLeaf(node.left, l)
            if(node.right is not None):
                checkLeaf(node.right, l)

        l1=[]
        l2=[]
        if(root1 is None or root2 is None):
            return False
        else:
            checkLeaf(root1, l1)
            checkLeaf(root2, l2)
            if(l1==l2):
                return True
            else:
                return False
