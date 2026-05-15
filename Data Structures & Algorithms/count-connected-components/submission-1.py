class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(v):
            visited.add(v)
            for neigh in adj[v]:
                if neigh == v or neigh in visited:
                    continue
                dfs(neigh)

        output = 0
        for i in range(n):
            if i in visited:
                continue
            output += 1
            dfs(i)
        return output