# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        else:
            self.traverse(root)

    def traverse(self, node):
        if node is None:
            return None
        left_end = self.traverse(node.left)
        right_end = self.traverse(node.right)

        if left_end is not None:
            left_end.right = node.right
            node.right = node.left
            node.left = None

        if right_end:
            return right_end
        elif left_end:
            return left_end
            
        return node

    




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    list_head = None
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            self.flatten(root.right)
            self.flatten(root.left)
            root.right = self.list_head
            root.left = None
            self.list_head = root
        
