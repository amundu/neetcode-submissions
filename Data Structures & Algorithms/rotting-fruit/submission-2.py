class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        minutes = 0
        fresh = 0

        def rot(r: int, c: int) -> None:
            nonlocal fresh
            if (r in range(ROWS)
            and c in range(COLS)
            and grid[r][c] == 1):
                grid[r][c] = 2
                q.append((r,c))
                fresh -= 1

        # Add rotten fruit coordinates to begin
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        while fresh > 0 and q:
            print(q)
            for i in range(len(q)):
                r, c = q.popleft()
                rot(r-1,c)
                rot(r+1,c)
                rot(r,c-1)
                rot(r,c+1)
            minutes+=1

        return minutes if not fresh else -1