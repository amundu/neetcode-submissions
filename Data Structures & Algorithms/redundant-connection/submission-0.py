class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = defaultdict(list)

        def dfs(v, parent):
            if visited[v]:
                return True
            visited[v] = True
            for neigh in adj[v]:
                if neigh == parent:
                    continue
                if dfs(neigh, v):
                    return True
            return False

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visited = [False] * (n+1)
            if dfs(u, 0):
                return [u,v]
        
