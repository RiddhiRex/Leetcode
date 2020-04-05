# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        #level order traversal and find empty nodes
        cur_lvl = [root]
        empty_spot = False
        while(len(cur_lvl)>0):
            nxt_lvl=[]
            for node in cur_lvl:
                if node is None:
                    empty_spot=True
                    continue
                if empty_spot==True:
                    return False
                nxt_lvl.append(node.left)
                nxt_lvl.append(node.right)
            cur_lvl = nxt_lvl
        return True
                
                
