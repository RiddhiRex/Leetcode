# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if root==None:
            return []
        self.ans = [root.val]
        def leftBoundary(node):
            if node is None or (node.left is None and node.right is None):
                return
            self.ans.append(node.val)
            if node.left is not None:
                leftBoundary(node.left)
            else:
                leftBoundary(node.right)
            
            
        def rightBoundary(node):
            if node is None or (node.left is None and node.right is None):
                return
            if node.right is not None:
                rightBoundary(node.right)
            else:
                rightBoundary(node.left)
            self.ans.append(node.val)
            
        def leaves(node):
            if node is None:
                return
            if node.left is None and node.right is None:
                self.ans.append(node.val)
            leaves(node.left)
            leaves(node.right)
        
        leftBoundary(root.left)
        leaves(root.left)
        leaves(root.right)
        rightBoundary(root.right) 
        return self.ans
