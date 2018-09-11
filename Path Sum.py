# Given a binary tree and a sum, 
#determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.result = False
        def pathSum(node, sum, currsum):
            if node.left is None and node.right is None:
                if(sum==currsum):
                    self.result = True
                    return self.result
            if(node.left is not None):
                pathSum(node.left, sum, currsum+node.left.val)
            if(node.right is not None):
                pathSum(node.right, sum, currsum+node.righat.val)
            return self.result
        if(root is not None):
            pathSum(root, sum, root.val)
            if(self.result):
                return True
            else:
                return False
        else:
            return False
                
