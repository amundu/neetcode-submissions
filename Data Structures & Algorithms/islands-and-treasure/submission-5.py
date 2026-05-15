class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        
        # BFS
        q = deque()
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append((row, col))

        steps = 0
        while q:
            steps += 1
            for _ in range(len(q)):
                row, col = q.popleft()
                directions = [(1,0), (-1,0), (0,1), (0,-1)]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if (nr in range(ROWS)
                    and nc in range(COLS)
                    and grid[nr][nc] == 2147483647):
                        grid[nr][nc] = steps
                        q.append((nr, nc))

        