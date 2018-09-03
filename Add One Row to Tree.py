# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def traverse(self, node, v, d, curd): 
        if(node is not None):
            if(curd==d-1):
                if(node.left is not None):
                    l = node.left
                    t = TreeNode(v)
                    node.left = t
                    t.left = l
                else:
                    l = TreeNode(v)
                    node.left = l
                    l.left = None
                    l.right = None

                if(node.right is not None):
                    r=node.right
                    t = TreeNode(v)
                    node.right = t
                    t.right = r
                else:
                    r = TreeNode(v)
                    node.right = r
                    r.left = None
                    r.right = None
            else:
                self.traverse(node.left, v, d, curd+1)
                self.traverse(node.right, v, d, curd+1)
        return 
    
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        node = root
        if(d==1):
            t = TreeNode(v)
            t.left = root
            return t
        self.traverse(node, v, d, 1)
        return root
    
                
            
                
            
            
            
        
