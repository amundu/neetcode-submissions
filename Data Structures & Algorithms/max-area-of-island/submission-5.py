class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0
        curr_area = 0
        def dfs(row, col):
            nonlocal curr_area
            if (
                row not in range(ROWS)
                or col not in range(COLS)
                or grid[row][col] != 1):
                    return
            curr_area += 1
            grid[row][col] = 'x'
            for dr, dc in [(1,0), (0,1)]:
                dfs(row+dr, col+dc)
                dfs(row-dr, col-dc)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    continue
                curr_area = 0
                dfs(row, col)
                max_area = max(max_area, curr_area)
        return max_area