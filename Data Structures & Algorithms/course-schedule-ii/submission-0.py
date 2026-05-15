class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjs_map = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adjs_map[course].append(prereq)

        visiting = set()
        visited = set()
        res = []
        def dfs(course: int) -> bool:
            if course in visiting:
                return False
            if course in visited:
                return True
            visiting.add(course)
            for prereq in adjs_map[course]:
                if not dfs(prereq):
                    return False
            res.append(course)
            visiting.remove(course)
            visited.add(course)
            return True
            
        for course in range(numCourses):
            if course not in visited and not dfs(course):
                return []
        return res