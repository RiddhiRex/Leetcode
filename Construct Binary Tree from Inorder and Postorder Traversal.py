# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        def dfs(inorder, postorder):
            root = TreeNode(postorder.pop())
            index = inorder.index(root.val)
        
            root.right = self.buildTree(inorder[index+1:], postorder)
            root.left = self.buildTree(inorder[:index], postorder)
            return root

        return dfs(inorder, postorder) 
        

solutioon2:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.io = inorder
        self.po = postorder
        def build(start, end):
            if(start<end):       
                root = TreeNode(self.po.pop())
                idx = self.io.index(root.val)
                root.right = build(idx+1, end)
                root.left = build(start, idx)

                return root
            
        return build(0, len(inorder))
