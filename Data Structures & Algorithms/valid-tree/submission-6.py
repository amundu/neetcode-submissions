class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjs_map = {i: [] for i in range(n)}

        for a, b in edges:
            adjs_map[a].append(b)
            adjs_map[b].append(a)

        visited = set()
        
        def dfs(node: int, prev_node: int) -> bool:
            if node in visited:
                return False
            visited.add(node)
            for next_node in adjs_map[node]:
                if next_node != prev_node and not dfs(next_node, node):
                    return False
            return True

        
        return dfs(0, -1) and n == len(visited)
                