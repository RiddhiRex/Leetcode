# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.ans = []
        def pathSum(node, sum, currsum, l):
            if node.left is None and node.right is None:
                if(currsum == sum):
                    return self.ans.append(l)
            if node.left is not None:
                pathSum(node.left, sum, currsum+node.left.val, l+[node.left.val])
            if node.right is not None:
                pathSum(node.right, sum, currsum+node.right.val, l+[node.right.val])
                
        if(root is None):
            return []
        else:
            l=[root.val]
            pathSum(root, sum, root.val, l)
            return self.ans
        
