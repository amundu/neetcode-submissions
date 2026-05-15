class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        inf = 2147483647

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append((row, col))
        steps = 0
        while q:
            steps += 1
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    next_row, next_col = row + dr, col + dc
                    if (
                        next_row in range(ROWS) and
                        next_col in range(COLS) and
                        grid[next_row][next_col] == inf):
                        grid[next_row][next_col] = steps
                        q.append((next_row, next_col))
