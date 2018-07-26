# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        curr = [root]
        ans = []
        while curr:
            l = []
            next_level = []
            for each in curr:
                l.append(each.val)
                if each.left is not None:
                    next_level.append(each.left)
                if each.right is not None:
                    next_level.append(each.right)
            ans.append(max(n for n in l))
            curr = next_level
        return ans
        
