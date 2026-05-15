class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        visited = set()

        graph = defaultdict(list)

        for u, v in edges:
            graph[v].append(u)
            graph[u].append(v)
        
        def dfs(node, parent):
            if node in visited:
                return True

            visited.add(node)
            for neigh in graph[node]:
                if neigh == parent:
                    continue
                if not dfs(neigh, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n