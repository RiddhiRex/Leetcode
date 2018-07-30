# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        node = root
        if(root is None):
            return TreeNode(val)
        while(node is not None):
            if(node.val<val):
                if(node.right is None):
                    temp = TreeNode(val)
                    node.right = temp
                    break
                else:
                    node = node.right
            elif(node.val>val):
                if(node.left is None):
                    temp = TreeNode(val)
                    node.left = temp 
                    break
                else:
                    node = node.left
        return root
