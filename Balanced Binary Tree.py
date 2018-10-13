# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getHeight(self, node):
        if node is None:
            return 0
        lh = self.getHeight(node.left)
        rh = self.getHeight(node.right)
        if lh<0 or rh<0 or abs(lh-rh)>1:
            return -1
        return max(lh, rh)+1
    
        
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return (self.getHeight(root)>=0)

        
        
