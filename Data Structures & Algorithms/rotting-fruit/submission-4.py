class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        total_fresh = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append((row, col))
                if grid[row][col] == 1:
                    total_fresh += 1

        minutes = 0
        while total_fresh and q:
            minutes += 1
            for _ in range(len(q)):
                row, col = q.popleft()
                directions = [(1,0), (-1,0), (0,1), (0,-1)]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (
                        nr in range(ROWS) and
                        nc in range(COLS) and 
                        grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        total_fresh -= 1
                        q.append((nr, nc))
        return minutes if total_fresh == 0 else -1

        