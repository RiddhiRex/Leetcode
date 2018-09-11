# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = []
        def traverse(node, depth):
            if node is None:
                return None
            if depth>len(ans):
                ans.append(node.val)
            traverse(node.left, depth+1)
            traverse(node.right, depth+1)
            
        if root is None:
            return None
        else:
            traverse(root, 1)
            return ans[-1]
        
