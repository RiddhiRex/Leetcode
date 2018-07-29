# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def validate(node, mini, maxi):
            if node is None:
                return True
            else:
                return node.val>mini and node.val<maxi and validate(node.left, mini, node.val) and validate(node.right, node.val , maxi)

        if(root is None):
            return True
        else:
            return validate(root, float("-inf"), float("inf"))
