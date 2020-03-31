# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs(node, pathsum):
            if node==None:
                return 0
            val = (pathsum==node.val) 
            val+= dfs(node.left, pathsum-node.val)
            val+= dfs(node.right, pathsum-node.val)
            return val
        
        if root==None:
            return 0
        ans = dfs(root, sum)
        ans += self.pathSum(root.left, sum)
        ans += self.pathSum(root.right, sum)
        return ans
