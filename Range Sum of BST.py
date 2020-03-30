# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        ans = 0
        if root == None:
            return 0
        if (root.val>R):
            ans += self.rangeSumBST(root.left, L, R)
        if(root.val<L):
            ans += self.rangeSumBST(root.right, L, R)
        if (L<=root.val<=R):
            ans += root.val+ self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
        return ans
            
