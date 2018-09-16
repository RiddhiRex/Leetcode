# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = []
        orderdict = {}
        ans = []
        queue.append([root, 0])
        while(len(queue)>0):
            item = queue.pop(0)
            node=item[0]
            hd=item[1]
            if hd not in orderdict:
                orderdict[hd]=[node.val]
            else:
                orderdict[hd].append(node.val)
            if node.left is not None:
                queue.append([node.left, hd-1])
            if node.right is not None:
                queue.append([node.right, hd+1])
        for k, v in sorted(orderdict.items()):
            ans.append(v)
        return ans
                
            
        
