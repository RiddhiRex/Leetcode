# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(node, ans):
            if node is None:
                return None
            else:
                traverse(node.left, ans)
                ans.append(node.val)
                traverse(node.right, ans)
            
            return None
        ans = []
        traverse(root, ans)
        prev = ans[0]
        minno = float("inf")
        for curr in ans[1:]:
            minno = min(minno , curr-prev)
            prev = curr
            if(minno==1):
                return minno
        return minno
