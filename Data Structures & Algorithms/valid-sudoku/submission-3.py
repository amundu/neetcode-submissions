class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_square_valid(i: int, j:int, size: int) -> bool:
            prev_vals = set()
            for k in range(size):
                for l in range(size):
                    if board[i + k][j + l] == ".":
                        continue
                    if board[i + k][j + l] in prev_vals:
                        return False
                    prev_vals.add(board[i + k][j + l])
            return True

        for i in range(len(board)):
            row_check = set()
            for j in range(len(board)):
                if board[i][j] in row_check:
                    return False
                if board[i][j] != ".":
                    row_check.add(board[i][j])
                

        for i in range(len(board)):
            column_check = set()
            for j in range(len(board)):
                if board[j][i] in column_check:
                    return False
                if board[j][i] != ".":
                    column_check.add(board[j][i])
        
        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                if not is_square_valid(i, j, 3):
                    return False
        
        return True
                

        