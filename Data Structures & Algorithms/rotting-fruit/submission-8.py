class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        def rot(r,c):
            nonlocal fresh
            if (
                r not in range(ROWS)
                or c not in range(COLS)
                or grid[r][c] != 1
            ):
                return
            grid[r][c] = 2
            q.append((r,c))
            fresh -= 1
        
        minutes = 0
        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()
                rot(r + 1, c)
                rot(r - 1, c)
                rot(r, c + 1)
                rot(r, c - 1)
            minutes += 1
        return minutes if fresh == 0 else -1 