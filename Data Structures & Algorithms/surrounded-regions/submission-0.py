class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(row, col):
            if (
                row in range(ROWS)
                and col in range(COLS)
                and board[row][col] == 'O'
            ):
                board[row][col] = 'T'
                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)


        for r in range(ROWS):
            for c in range(COLS):
                if ((r == 0 or r == ROWS-1) or (c == 0 or c == COLS-1)) and board[r][c] == 'O':
                    dfs(r, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'
