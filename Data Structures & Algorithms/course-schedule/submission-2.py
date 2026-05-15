class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        completed = set()
        visited = set()

        prerequisites_map = defaultdict(list)

        for prerequisite in prerequisites:
            prerequisites_map[prerequisite[0]].append(prerequisite[1])

        def can_complete(course):
            if course in completed:
                return True
            if course in visited:
                return False
            visited.add(course)
            for prereq in prerequisites_map[course]:
                if not can_complete(prereq):
                    return False
            visited.remove(course)
            completed.add(course)
            return True

        for course in range(numCourses):
            if not can_complete(course):
                return False
        return numCourses == len(completed)

        

        
        