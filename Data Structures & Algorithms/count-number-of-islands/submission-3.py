class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def bfs(root_row, root_col):
            q = deque()
            q.append((root_row, root_col))

            while q:
                row, col = q.popleft()
                grid[row][col] = '0'

                directions = [(1,0), (-1,0), (0,1), (0,-1)]
                for dr, dc in directions:
                    nr, nc = dr+row, dc+col
                    if (nr not in range(ROWS) or nc not in range(COLS) or grid[nr][nc] == '0'):
                        continue
                    q.append((nr, nc))

        
        total = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    total += 1
                    bfs(row, col)
        return total