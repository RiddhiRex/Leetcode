# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

class Solution(object):
    
    def ordering(self, node):
        if node!=None:
            order=self.ordering(node.left)+self.ordering(node.right)+str(node.val)
            self.dic[order].append(node)
            return order
        else:
            return "*"
    
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        self.dic = collections.defaultdict(list)
        if root==None:
            return []
        self.dic[self.ordering(root.left)+self.ordering(root.right)+str(root.val)].append(root)
        ans = []
        for k, v in self.dic.items():
            if len(v)>1:
                ans.append(v[0])
        return ans
        
