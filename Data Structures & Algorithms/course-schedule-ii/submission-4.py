class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = defaultdict(set)

        for n in range(numCourses):
            pre_map[n] = set()

        for course, prereq in prerequisites:
            pre_map[course].add(prereq)

        visiting = set()
        visited = set()
        output = []

        def dfs(course):
            if course in visited:
                return True
            if course in visiting:
                return False
            
            visiting.add(course)
            for prereq in pre_map[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)
            visited.add(course)
            output.append(course)
            return True
        
        for course in pre_map:
            if not dfs(course):
                return []
        return output
            