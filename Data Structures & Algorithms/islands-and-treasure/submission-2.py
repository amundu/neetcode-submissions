class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    q.append((r,c))

        def add_room(r: int, c: int) -> None:
            if (r < 0 or c < 0
            or r == ROWS or c == COLS
            or grid[r][c] == -1
            or (r,c) in visited):
                return
            visited.add((r,c))
            q.append((r,c))

        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                add_room(r-1,c)
                add_room(r+1,c)
                add_room(r,c-1)
                add_room(r,c+1)
            
            distance +=1