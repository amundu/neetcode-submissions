class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        res = []
        atlantic = set()
        pacific = set()

        def dfs(r: int, c: int, visited: set, prev: int) -> None:
            if ((r,c) in visited
            or r not in range(ROWS)
            or c not in range(COLS)
            or prev > heights[r][c]
            ):
                return
            visited.add((r,c))
            dfs(r-1, c, visited, heights[r][c])
            dfs(r+1, c, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
        
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS-1, c, atlantic, heights[ROWS-1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS-1, atlantic, heights[r][COLS-1])

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atlantic and (r,c) in pacific:
                    res.append((r,c))      
        return res
            