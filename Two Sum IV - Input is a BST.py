# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.l = []
        self.k = k
        def traverse(node):
            if node is None:
                return None
            if(node.left is not None):
                traverse(node.left)
            self.l.append(node.val)
            if(node.right is not None):
                traverse(node.right)
        
        traverse(root)
        i=0
        l =self.l
        j = len(l)-1
        print(l)
        while(i<j):
            print(l[i]+l[j])
            if(l[i]+l[j]<k):
                i+=1
            elif(l[i]+l[j]>k):
                j-=1
            elif(l[i]+l[j]==k):
                return True
        return False
                
            
            
            
