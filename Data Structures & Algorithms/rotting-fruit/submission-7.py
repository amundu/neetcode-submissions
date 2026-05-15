class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        
        total = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    continue
                if grid[r][c] == 2:
                    q.append((r,c))
                total += 1

        def rot(r,c):
            if (
                r not in range(ROWS)
                or c not in range(COLS)
                or grid[r][c] != 1
            ):
                return
            grid[r][c] = 2
            q.append((r,c))
        
        if total == 0:
            return 0
        
        minutes = -1
        rotten_fruit = 0
        while q:
            for _ in range(len(q)):
                rotten_fruit += 1
                r, c = q.popleft()
                rot(r + 1, c)
                rot(r - 1, c)
                rot(r, c + 1)
                rot(r, c - 1)
            minutes += 1
        return minutes if rotten_fruit == total else -1 