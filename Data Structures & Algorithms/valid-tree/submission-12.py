class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        par = {}
        rank = {}

        for i in range(n):
            par[i] = i
            rank[i] = 0

        def find(node):
            curr = node
            while curr != par[curr]:
                par[curr] = par[par[curr]]
                curr = par[curr]
            return curr

        def union(n1, n2):
            par1, par2 = find(n1), find(n2)
            if par1 == par2:
                return False

            if rank[par1] > rank[par2]:
                par[par2] = par1
            elif rank[par1] < rank[par2]:
                par[par1] = par2
            else:
                par[par2] = par1
                rank[par1] += 1
            return True
        
        union_cnt = 0
        for u, v in edges:
            if not union(u, v):
                return False
            union_cnt += 1
        return union_cnt == n-1