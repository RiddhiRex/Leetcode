# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import operator
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def traverse(node, dic):
            if node is None:
                return None
            else:
                if node.val not in dic.keys():
                    dic[node.val]=1
                else:
                    dic[node.val]+=1
                traverse(node.left, dic)
                traverse(node.right, dic)
                
            return None
        dic = {}
        if root is None:
            return []
        else:
            traverse(root, dic)
            maxval = max(dic.values())

            return [k for k in dic.keys() if dic[k]==maxval]
          
        
