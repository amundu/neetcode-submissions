class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses_to_prerequisites = defaultdict(set)

        for course, prerequisite in prerequisites:
            courses_to_prerequisites[course].add(prerequisite)
        
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if course not in courses_to_prerequisites:
                return True
            visiting.add(course)
            for prereq in courses_to_prerequisites[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)
            return True

        for course in courses_to_prerequisites.keys():
            if not dfs(course):
                return False 

        return True