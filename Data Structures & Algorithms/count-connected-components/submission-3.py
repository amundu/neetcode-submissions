class DSU:
    def __init__(self, n):
        self.par = {}
        self.rank = {i:0 for i in range(n)}
        self.components = n

        for i in range(n):
            self.par[i] = i
    
    def find(self, v):
        curr = v
        while self.par[curr] != curr:
            self.par[curr] = self.par[self.par[curr]]
            curr = self.par[curr]
        return curr
    
    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2:
            return
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
        self.components -= 1

    def get_components(self):
        return self.components


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)

        for u, v in edges:
            dsu.union(u,v)
        return dsu.get_components()