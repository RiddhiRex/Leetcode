class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
class solution(object):    
    def traverse(self, st, i):
        start = i
        if(st[i])=='-':
            i+=1
        while(i<len(st) and st[i].isdigit()):
            i+=1
        root= TreeNode(int(st[start:i]))
        i+=1
        if i<len(st) and st[i]=="(":
            i+=1
            root.left, i = self.traverse(st, i)
            i+=1
        if i<len(st) and st[i]=="(":
            i+=1
            root.right, i = self.traverse(st, i)
            i+=1
        return root, i 
        
    def stToBinaryTree(self, st):
        if len(st)==0 or st=="()":
            return None
        return self.traverse(st, 0)[0]

if __name__=="__main__":
    self=solution()
    st = "4(2(3)(1))(6(5))"
    root = self.stToBinaryTree(st)
