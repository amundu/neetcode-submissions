class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(row, col):
            if row not in range(ROWS) or col not in range(COLS) or grid[row][col] == '0':
                return
            directions = [(1,0), (0,1)]
            grid[row][col] = '0'
            for dr, dc in directions:
                dfs(row+dr, col + dc)
                dfs(row-dr, col - dc)


        total = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '0':
                    continue
                dfs(row, col)
                total += 1
        return total