# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def finddepth(node, depth):
            if node.left is None and node.right is None:
                self.maxdepth = max(depth, self.maxdepth)
                return 
            if node.left is not None:
                finddepth(node.left, depth+1)
            if node.right is not None:
                finddepth(node.right, depth+1)
            return
        
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        self.maxdepth = 1
        finddepth(root, 1)
        return self.maxdepth
        
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root is None):
            return 0
        if(root.right ==None):
            return self.maxDepth(root.left)+1
        if(root.left ==None):
            return self.maxDepth(root.right)+1
        else:
            return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)
        
        
