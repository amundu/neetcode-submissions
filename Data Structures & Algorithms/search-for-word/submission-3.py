class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        path = set()
        ROWS, COLS = len(board), len(board[0])

        def dfs(i, row, col):
            if i == len(word):
                return True
            if (
                row not in range(ROWS)
                or col not in range(COLS)
                or (row, col) in path
                or board[row][col] != word[i]
            ):
                return False
            directions = [(1,0), (0,1), (-1,0), (0,-1)]
            path.add((row, col))
            for dr, dc in directions:
                if dfs(i + 1, row + dr, col + dc):
                    return True
            path.remove((row, col))
            return False
            
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(0, row, col):
                    return True
        return False