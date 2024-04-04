# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def traversedelete(node, key):
            if node is None:
                return None
           
            if node.val>key:
                node.left = traversedelete(node.left, key)
            elif node.val<key:
                node.right = traversedelete(node.right, key)
            else:
                if node.left is None and node.right is None:
                    return None
                elif node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                else:
                    tmp_node = node.right
                    while(tmp_node.left!=None):
                        tmp_node = tmp_node.left
                    node.val = tmp_node.val
                    node.right = traversedelete(node.right, tmp_node.val)
            return node
          
        return traversedelete(root, key)
            
                
                


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if(root is None):
            return root
        elif root.val<key:
            root.right = self.deleteNode(root.right, key)
        elif root.val>key:
            root.left = self.deleteNode(root.left, key)
        else:

            if(root.left is None):
                right = root.right
                del root
                return right
            elif(root.right is None):
                left = root.left
                del root
                return left
            else:
                tmp = root.right
                while(tmp.left):
                    tmp = tmp.left
                root.val = tmp.val
                root.right = self.deleteNode(root.right, tmp.val)
        return root
                
