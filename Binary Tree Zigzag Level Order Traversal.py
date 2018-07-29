# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.ans = []
        def traverse(root):
            if(root is None):
                return None
            else:
                curr = [root]
                while(len(curr)!=0):
                    lvl = []
                    next_level = []
                    for node in curr:
                        lvl.append(node.val)
                        if(node.left is not None):
                            next_level.append(node.left)
                        if(node.right is not None):
                            next_level.append(node.right)
                    curr = next_level
                    self.ans.append(lvl)

        if root is None:
            return []
        else:
            traverse(root)
            for i in range(len(self.ans)):
                if i%2!=0:
                    self.ans[i]=self.ans[i][::-1]
            return self.ans
        
