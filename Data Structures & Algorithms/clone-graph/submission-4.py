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
        og_to_copy = {}

        def dfs(root):
            if root in og_to_copy:
                return
            copy = Node(root.val)
            og_to_copy[root] = copy
            for neigh in root.neighbors:
                dfs(neigh)
                copy.neighbors.append(og_to_copy[neigh])
        dfs(node)
        return og_to_copy[node]