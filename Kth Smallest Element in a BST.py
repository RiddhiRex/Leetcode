# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def traverse(node, l):
            if node is None:
                return None
            else:
                if node.val not in l:
                    l.append(node.val)
                traverse(node.left, l)
                traverse(node.right, l)
                
            return None
        l = []
        if root is None:
            return []
        else:
            traverse(root, l)
            return sorted(l)[k-1]
