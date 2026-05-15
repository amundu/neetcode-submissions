class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        visited = set()

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        print(adj)
        def dfs(v, prev):
            visited.add(v)
            print(visited)
            for neigh in adj[v]:
                if neigh == prev:
                    continue
                if neigh in visited or not dfs(neigh, v):
                    print(neigh, v)
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n