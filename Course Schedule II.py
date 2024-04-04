class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dict = collections.defaultdict(list)
        for course, prereq in prerequisites:
            dict[course].append(prereq)
        visited = set()
        ans = []
        cycle = set()
        def dfs(course):
            if course in visited:
                return True
            if course in cycle:
                return False
            
            cycle.add(course)
            for c in dict[course]:
                if c not in visited:
                    if dfs(c)==False:
                        return False
            visited.add(course)
            ans.append(course)
            cycle.remove(course)
            return True
            
        for k in range(numCourses):
            if k not in visited:
                if dfs(k)==False:
                    return []
        return ans
            
                    
                    
                
                        
                    
