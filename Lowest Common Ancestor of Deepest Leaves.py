# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def dfs_search(node):
            if node is None:
                return 0, None
            d1, ancestor1 = dfs_search(node.left)
            d2, ancestor2 = dfs_search(node.right)  
            if d1>d2:
                return d1+1, ancestor1
            elif d2>d1:
                return d2+1, ancestor2
            else:
                return d1+1, node
        return dfs_search(root)[1]
            
        
