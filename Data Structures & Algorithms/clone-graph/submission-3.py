"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.nodes_map = {}
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        if node.val in self.nodes_map:
            return self.nodes_map[node.val]

        self.nodes_map[node.val] = Node(node.val)
        for neighbor in node.neighbors:
            self.nodes_map[node.val].neighbors.append(self.cloneGraph(neighbor))
        return self.nodes_map[node.val]
        