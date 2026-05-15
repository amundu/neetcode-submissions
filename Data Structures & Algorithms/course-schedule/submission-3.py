class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visiting = set()

        pre_map = defaultdict(list)

        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        def can_complete(course):
            if not pre_map[course]:
                return True
            if course in visiting:
                return False
            visiting.add(course)
            for prereq in pre_map[course]:
                if not can_complete(prereq):
                    return False
            visiting.remove(course)
            return True

        for course in range(numCourses):
            if not can_complete(course):
                return False
        return True

        

        
        