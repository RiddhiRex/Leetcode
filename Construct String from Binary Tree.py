# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def traverse(self, t, st):
        if t is None:
            return None
        st.append(str(t.val))
        if(t.left is not None or t.right is not None):
            st.append("(")
            if(t.left is not None):
                self.traverse(t.left, st)
            st.append(")")
            if(t.right is not None):
                st.append("(")
                self.traverse(t.right, st)
                st.append(")")
        return st
                
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        string = self.traverse(t, [])
        if(string is not None):
            return "".join(string)
        else:
            return ""

        
