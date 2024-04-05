class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def dfs(course):
            if course in seen:
                return True
            if course in cycle:
                return False
            cycle.add(course)
            for c in dict[course]:
                if c not in seen:
                    if dfs(c)==False:
                        return False
            cycle.remove(course)
            seen.add(course)
            return True
        
        seen = set()
        cycle = set()
        dict = collections.defaultdict(list)
        for p in prerequisites:
            dict[p[0]].append(p[1])
        
        for i in range(numCourses):
            if i not in seen:
                if dfs(i)==False:
                    return False
        return True
        
        


#Solution 2:
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(node, path, pre_req):
            if node in path:
                return False
            if node in visited:
                return None
            
            visited.add(node)
            path.add(node)
 
            if node in pre_req:
                for each in pre_req[node]:
                    if dfs(each, path, pre_req)==False:
                          return False
                        
            path.remove(node)
            return True
            
        
        pre_req = {}
        for a, b in prerequisites:
            if a not in pre_req.keys():
                pre_req[a]=[]
            pre_req[a].append(b)

        visited = set()
        for k, v in pre_req.items():
            if k not in visited:
                if dfs(k, set(), pre_req)==False:
                    return False
        return True
