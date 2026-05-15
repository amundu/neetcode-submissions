class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        
        # BFS
        q = deque()
        visited = set()
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append((row, col, 0))
                    visited.add((row, col))

        while q:
            row, col, steps = q.popleft()
            grid[row][col] = steps
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if (nr not in range(ROWS)
                or nc not in range(COLS)
                or grid[nr][nc] == -1
                or (nr, nc) in visited):
                    continue

                visited.add((nr, nc))
                q.append((nr, nc, steps + 1))

        