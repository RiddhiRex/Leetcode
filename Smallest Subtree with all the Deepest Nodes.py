# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node, parent=None):
            if node is None:
                return
            depth[node]=depth[parent]+1
            dfs(node.left, node)
            dfs(node.right, node)
        
        def getMaxDepthParent(node):
            if node is None:
                return None
            if depth[node]==maxdepth:
                return node
            l = getMaxDepthParent(node.left)
            r = getMaxDepthParent(node.right)
            if l!=None and r!=None:
                return node
            elif l==None:
                return r
            else:
                return l
            
        depth={}
        depth[None]=-1
        dfs(root, None)
        maxdepth = max(depth.values())
        return getMaxDepthParent(root)
        
        
