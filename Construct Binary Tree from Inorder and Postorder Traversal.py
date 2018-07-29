# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.io = inorder
        self.po = postorder
        def build(start, end):
            if(start<end):       
                root = TreeNode(self.po.pop())
                idx = self.io.index(root.val)
                root.right = build(idx+1, end)
                root.left = build(start, idx)

                return root
            
        return build(0, len(inorder))
