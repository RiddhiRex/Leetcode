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
        ans = []
        if root is None:
            return ""
        cur_lvl = [root]
        while(cur_lvl):
            tmp_ans = []
            nxt_lvl = []
            for node in cur_lvl:
                if node is not None:
                        tmp_ans.append(str(node.val))
                        nxt_lvl.append(node.left)
                        nxt_lvl.append(node.right)
                else:
                    tmp_ans.append("*")


            ans.append(",".join(tmp_ans))       
            cur_lvl = nxt_lvl
        print(";".join(ans))
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
            print("jere")
            for i,v in enumerate(vals):
                if v!="*":
                    node = TreeNode(int(v))
                    print(i)
                    if(i%2)==0:
                        prev_lvl[i//2].left=node
                    else:
                        prev_lvl[i//2].right=node
                    curr_lvl.append(node)   
            prev_lvl= curr_lvl

        return root



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
