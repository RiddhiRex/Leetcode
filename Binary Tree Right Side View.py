# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def rightView(node, depth, l):
            if(node is None):
                return None
            if (depth>len(l)):
                l.append(node.val)
            rightView(node.right, depth+1, l)
            rightView(node.left, depth+1, l)
            
        l = []  
        if(root is None):
            return l
        else:
            rightView(root, 1, l)
        return l
        
