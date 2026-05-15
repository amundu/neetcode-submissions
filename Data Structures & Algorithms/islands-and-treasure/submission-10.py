class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))

        def add(r,c):
            if (
                r not in range(ROWS)
                or c not in range(COLS)
                or grid[r][c] != 2147483647
            ):
                return
            q.append((r, c))
            grid[r][c] = 'x' # marked to be explored

        distance = 0
        while q:
            for _ in range(len(q)):
                (r, c) = q.popleft()
                grid[r][c] = distance
                add(r + 1, c)
                add(r - 1, c)
                add(r, c + 1)
                add(r, c - 1)
            distance += 1
