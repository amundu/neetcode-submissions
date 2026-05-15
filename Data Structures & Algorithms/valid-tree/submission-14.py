class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        visited = set()

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def dfs(v, prev):
            visited.add(v)
            for neigh in adj[v]:
                if neigh == prev:
                    continue
                if neigh in visited or not dfs(neigh, v):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n