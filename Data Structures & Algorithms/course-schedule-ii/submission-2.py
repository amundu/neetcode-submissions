class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        visited = set()
        visiting = set()
        output = []
        def dfs(crs: int) -> bool:
            if crs in visiting:
                return False
            if crs in visited:
                return True
            
            visiting.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return output
            