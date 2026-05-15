class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisites_map = {i: [] for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            prerequisites_map[course].append(prerequisite)

        visiting = set()
        visited = set()
        def dfs(course: int) -> bool:
            if course in visiting:
                return False
            visiting.add(course)
            for prerequisite in prerequisites_map[course]:
                if not dfs(prerequisite):
                    return False
                
            visiting.remove(course)
            visited.add(course)
            return True
        
        for course in range(numCourses):
            if course not in visited:
                if not dfs(course):
                    return False
        return True