class Solution:
    def simplifyPath(self, path: str) -> str:
        directory = path.split("/")
        stack = []
        print(directory)
        for d in directory:
            if d=="..":
                if len(stack)>0:
                    stack.pop()
            elif d in [".",""]:
                continue
            else:
                stack.append(d)
        return "/"+"/".join(stack)
            
                
