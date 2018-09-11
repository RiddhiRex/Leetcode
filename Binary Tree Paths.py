# Given a binary tree, return all root-to-leaf paths.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        soln = []
        def traverse(root, path):
            if root is None:
                return soln
            if(root.left is None and root.right is None):
                return soln.append(path)
            if(root.left is not None):
                traverse(root.left, str(path)+"->"+str(root.left.val))   
            if(root.right is not None):
                traverse(root.right, str(path)+"->"+str(root.right.val))

        if(root is not None):
            traverse(root, str(root.val))
        return soln
        
