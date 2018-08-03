# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        def getDepth(node):
            if node is None:
                return 0
            else:
                return max(getDepth(node.left), getDepth(node.right))+1
        d1 = getDepth(root.left)+getDepth(root.right)
        ld = self.diameterOfBinaryTree(root.left)
        rd = self.diameterOfBinaryTree(root.right)
        return max(d1, ld, rd)
        

        
