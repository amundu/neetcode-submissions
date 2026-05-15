class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_set = set()
        atlantic_set = set()

        ROWS, COLS = len(heights), len(heights[0])

        def dfs(row, col, prev_height, curr_set):
            if (
                row not in range(ROWS)
                or col not in range(COLS)
                or prev_height > heights[row][col]
                or (row, col) in curr_set
            ):
                return
            
            curr_set.add((row, col))
            directions = [(1,0), (0,1), (-1,0), (0,-1)]
            for dr, dc in directions:
                dfs(row+dr, col+dc, heights[row][col], curr_set)
            
        
        for row in range(ROWS):
            for col in range(COLS):
                if row == 0 or col == 0:
                    dfs(row, col, 0, pacific_set)

        for row in range(ROWS):
            for col in range(COLS):
                if row == ROWS-1 or col == COLS-1:
                    dfs(row, col, 0, atlantic_set)

        output = []
        for row, col in pacific_set:
            if (row, col) in atlantic_set:
                output.append([row, col])
        return output