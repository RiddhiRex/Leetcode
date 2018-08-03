# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def dfs(node, no):
            if node.left is None and node.right is None:
                self.ans = self.ans+int(no+str(node.val))
            else:
                no = no+str(node.val)
                if(node.left is not None):
                    dfs(node.left, no)
                if(node.right is not None):
                    dfs(node.right, no)
        if(root is None):
            return 0
        dfs(root, "0")
        return self.ans
            
        
