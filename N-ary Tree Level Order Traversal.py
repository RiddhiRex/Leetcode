"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        curr = [root]
        ans = []
        while curr:
            next_level = []
            l = []
            for each in curr:
                l.append(each.val)
                if each.children is not None:
                    for i in each.children:
                        next_level.append(i)
            ans.append(l)
            curr = next_level
        return ans
