class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()

        def dfs(row, col):
            if (row not in range(ROWS)
            or col not in range(COLS)
            or (row, col) in visited
            or grid[row][col] == 0):
                return 0
            
            visited.add((row, col))
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            area = 1
            for dr, dc in directions:
                area += dfs(row + dr, col + dc)
            return area
        
        max_area = 0
        for row in range(ROWS):
            for col in range(COLS):
                max_area = max(max_area, dfs(row, col))

        return max_area
