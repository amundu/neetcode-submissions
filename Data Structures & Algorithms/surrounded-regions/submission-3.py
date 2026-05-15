class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(row, col):
            if (
                row not in range(ROWS)
                or col not in range(COLS)
                or board[row][col] != 'O'
            ):
                return
            board[row][col] = '#'
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                dfs(row+dr, col+dc)
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'X':
                    continue
                if row == 0 or row == ROWS-1 or col == 0 or col == COLS-1:
                    dfs(row, col)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                if board[row][col] == '#':
                    board[row][col] = 'O'