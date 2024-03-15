# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def traverse(node, target):
            if node==None:
                return
            if node.val==target:
                self.closest = node.val
                self.mindiff = 0
                return
            diff = abs(target-node.val)
            if diff< self.mindiff or (diff==self.mindiff and node.val<self.closest):
                self.closest = node.val
                self.mindiff = diff
            if node.val>target:
                traverse(node.left, target)
            else:
                traverse(node.right, target)
            return

        self.mindiff = float("inf")
        self.closest = 0
        traverse(root, target)
        return self.closest


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
'''
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if root is None:
            return float('inf')

        if root.val == target:
            return root.val
        elif root.val < target:
            rightRes = self.closestValue(root.right, target)
            return root.val if abs(root.val - target) < abs(rightRes - target) else rightRes
        elif root.val > target:
            leftRes = self.closestValue(root.left, target)
            return root.val if abs(root.val - target) < abs(leftRes - target) else leftRes
