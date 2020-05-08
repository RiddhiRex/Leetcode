class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        color = {}
        for i in range(len(graph)):
            if i in color:
                continue
            color[i]=0
            stack = [i]
            while(len(stack)>0):
                idx = stack.pop(0)
                for each in graph[idx]:
                    if each not in color:
                        color[each]=color[idx]^1
                        stack.insert(0, each)
                    elif color[each]==color[idx]:
                        return False
        return True
                    
            
