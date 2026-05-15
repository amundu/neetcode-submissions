class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjs_map = {i: [] for i in range(n)}

        for a, b in edges:
            adjs_map[a].append(b)
            adjs_map[b].append(a)

        visiting, visited = set(), set()
        
        def dfs(node: int, prev_node: int) -> bool:
            if node in visiting:
                return False
            if node in visited:
                return True
            visiting.add(node)
            for next_node in adjs_map[node]:
                if next_node != prev_node and not dfs(next_node, node):
                    return False
            visiting.remove(node)
            visited.add(node)
            return True

        print(adjs_map)
        if 0 not in visited and not dfs(0, -1):
            return False
        return n == len(visited)
                