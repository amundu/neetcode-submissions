class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(row: int, col: int) -> None:
            if (
                row not in range(ROWS) or
                col not in range(COLS) or
                grid[row][col] == "0"):
                return
            grid[row][col] = "0"
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
        
        islands_count = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    islands_count += 1
                    dfs(row, col)
        return islands_count