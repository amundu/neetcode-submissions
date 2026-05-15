class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        # colum check
        for row in range(len(board)):
            for col in range(len(board[0])):
                digit = board[row][col]
                if digit == '.':
                    continue

                s_row, s_col = row // 3, col // 3
                if (
                    digit in rows[row] 
                    or digit in cols[col] 
                    or digit in squares[(s_row,s_col)]
                    ):
                    return False
                
                rows[row].add(digit)
                cols[col].add(digit)
                squares[(s_row, s_col)].add(digit)
        return True
                