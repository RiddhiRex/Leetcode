"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        self.ans = []
        self.traverse(root)
        return self.ans
    
    def traverse(self, node):
        if node is not None:
            if(node.children is not None):
                    for each in node.children:
                        self.traverse(each)
            self.ans.append(node.val)    
