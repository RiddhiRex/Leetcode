# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preorder = preorder
        self.inorder = inorder
        def build(start, end):
            if start<end:
                root = TreeNode(self.preorder.pop(0))
                idx = self.inorder.index(root.val)
                root.left = build(start, idx)
                root.right = build(idx+1, end)
                return root
        return build(0, len(self.inorder))
        
