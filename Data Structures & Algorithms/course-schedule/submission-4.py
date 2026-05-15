class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses_to_prerequisites = defaultdict(set)
        for n in range(numCourses):
            courses_to_prerequisites[n] = set()

        for course, prerequisite in prerequisites:
            courses_to_prerequisites[course].add(prerequisite)
        
        visited = set()
        path = set()

        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True
            path.add(course)
            for prereq in courses_to_prerequisites[course]:
                if not dfs(prereq):
                    return False
            path.remove(course)
            visited.add(course)
            return True

        for course in courses_to_prerequisites.keys():
            if not dfs(course):
                return False 

        return True