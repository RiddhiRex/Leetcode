# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        self.ans = []
        def traverse(root):
            if root is None:
                return None
            curr = [root]
            while(len(curr)!=0):
                l =[]
                next_lvl = []
                for node in curr:
                    l.append(node.val)
                    if(node.left is not None):
                        next_lvl.append(node.left)
                    if(node.right is not None):
                        next_lvl.append(node.right)
                self.ans.append(float(sum(l))/len(l))
                curr = next_lvl
        traverse(root)
        return self.ans
        
