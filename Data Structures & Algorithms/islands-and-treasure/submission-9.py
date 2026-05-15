class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        
        def add(r,c):
            if (
                r not in range(ROWS)
                or c not in range(COLS)
                or grid[r][c] != 2147483647
            ):
                return
            q.append((r, c))
            grid[r][c] = 'x' # marked to be explored

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        distance = 0
        while q:
            for _ in range(len(q)):
                (r, c) = q.popleft()
                grid[r][c] = distance
                directions = [(1,0), (0,1), (-1,0), (0,-1)]
                for dr, dc in directions:
                    add(r+dr,c+dc)
                    
            distance += 1
