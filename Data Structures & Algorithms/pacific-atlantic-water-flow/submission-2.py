class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        def dfs(row, col, visit, prev_height):
            if (
                (row, col) in visit
                or row not in range(ROWS)
                or col not in range(COLS)
                or heights[row][col] < prev_height):
                return 
            visit.add((row, col))
            dfs(row + 1, col, visit, heights[row][col])
            dfs(row - 1, col, visit, heights[row][col])
            dfs(row, col + 1, visit, heights[row][col])
            dfs(row, col - 1, visit, heights[row][col])

        pacific_set = set()
        atlantic_set = set()
        for row in range(ROWS):
            for col in range(COLS):
                if row == 0 or col == 0:
                    dfs(row, col, pacific_set, heights[row][col])
                if row == len(heights)-1 or col == len(heights[0])-1:
                    dfs(row, col, atlantic_set, heights[row][col])

        output = []
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in pacific_set and (row, col) in atlantic_set:
                    output.append([row, col])
        
        return output