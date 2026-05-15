"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        visited = set()
        copy_map = defaultdict(lambda: Node())
        stack = [node]
        while stack:
            original = stack.pop()
            if original in visited:
                continue
            visited.add(original)
            copy = copy_map[original.val]
            copy.val = original.val
            for neighbor in original.neighbors:
                stack.append(neighbor)
                copy.neighbors.append(copy_map[neighbor.val])
        return copy_map[node.val]


        