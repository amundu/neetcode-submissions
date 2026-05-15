class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisites_map = defaultdict(list)
        for course, prerequisite in prerequisites:
            prerequisites_map[course].append(prerequisite)

        for i in range(numCourses):
            if i not in prerequisites_map:
                prerequisites_map[i] = []
        
        visiting = set()
        visited = set()
        def dfs(course: int) -> bool:
            if course in visited:
                return True
            
            if course in visiting:
                return False
            visiting.add(course)
            print(course)
            for prerequisite in prerequisites_map[course]:
                if not dfs(prerequisite):
                    return False
                
            visiting.remove(course)
            visited.add(course)
            return True
        
        for course in prerequisites_map.keys():
            if course not in visited:
                if not dfs(course):
                    return False
        return len(visited) == numCourses