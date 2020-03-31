# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.idx=-1
        self.inorder_list = []
        self.inorder(root)
        
    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        self.inorder_list.append(node.val)
        self.inorder(node.right)
        return
    
    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.idx+=1
        return self.inorder_list[self.idx]
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.idx+1<len(self.inorder_list):
            return True
        else:
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
