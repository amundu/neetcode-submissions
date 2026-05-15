class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        distance = 0
        while q:
            for _ in range(len(q)):
                (r, c) = q.popleft()
                grid[r][c] = distance
                directions = [(1,0), (0,1), (-1,0), (0,-1)]
                for dr, dc in directions:
                    new_r, new_c = r+dr, c+dc
                    if (
                        new_r not in range(ROWS)
                        or new_c not in range(COLS)
                        or grid[new_r][new_c] != 2147483647
                    ):
                        continue
                    q.append((new_r, new_c))
                    grid[new_r][new_c] = 'x'
            distance += 1
