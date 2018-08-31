# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def traverse(self, node, lis):
            if node is None:
                return None
            else:
                lis.append(node.val)
                self.traverse(node.left, lis)
                self.traverse(node.right, lis)
                return lis
            
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodes = self.traverse(root, [])
        print(nodes)
        if(len(set(nodes))>1):
            return sorted(set(nodes))[1]
        else:
            return -1
        
            
