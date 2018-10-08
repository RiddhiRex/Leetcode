# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        if root is None:
            return ""
        curr_lvl=[root]
        next_lvl = []
        ans =[]

        while(curr_lvl):
            tmp_ans = ",".join(str(node.val) if node is not None else "*" for node in curr_lvl)
            ans.append(tmp_ans)
            nxt_lvl = []
            for each in curr_lvl:
                if each is not None:
                    nxt_lvl.append(each.left)  
                    nxt_lvl.append(each.right)

            curr_lvl=nxt_lvl

        return ";".join(ans)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if(len(data)==0):
            return None
        
        lvls = data.split(";")
        root = TreeNode(int(lvls[0]))
        prev_lvl=[root]

        for i in range(1, len(lvls)):
            curr_lvl=[]
            vals = lvls[i].split(",")
            
            for i,v in enumerate(vals):
                if v!="*":
                    node = TreeNode(int(v))
                    if(i%2)==0:
                        prev_lvl[i//2].left=node
                    else:
                        prev_lvl[i//2].right=node
                    curr_lvl.append(node)   
            prev_lvl= curr_lvl

        return root

                
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
