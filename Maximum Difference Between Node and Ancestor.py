# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(node):
            if node is None:
                return float("inf"), float("-inf")
            minl, maxl = dfs(node.left)
            minr, maxr = dfs(node.right)
            mini = min(minl, minr)
            maxi = max(maxl, maxr)
            if mini!=float("inf"):
                self.ans = max(self.ans , abs(mini-node.val))
            if maxi!=float("-inf"):
                self.ans = max(self.ans, abs(maxi-node.val))
            return min(mini, node.val), max(maxi, node.val)
        self.ans = 0
        dfs(root)
        return self.ans
                
