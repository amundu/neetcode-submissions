class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()
        total_fruits = 0

        def add_cell(r: int, c: int) -> None:
            if (r < 0 or c < 0 
            or r == ROWS or c == COLS 
            or (r,c) in visited 
            or grid[r][c] == 0):
                return
            visited.add((r,c))
            q.append((r,c))

        # Add rotten fruit coordinates to begin
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    total_fruits+=1
                    q.append((r,c))
                    visited.add((r,c))
                if grid[r][c] == 1:
                    total_fruits+=1

        if not total_fruits:
            return 0
        
        minutes = -1
        while q:
            print(q)
            for i in range(len(q)):
                r, c = q.popleft()
                add_cell(r-1,c)
                add_cell(r+1,c)
                add_cell(r,c-1)
                add_cell(r,c+1)
            minutes+=1

        return minutes if len(visited) == total_fruits else -1