class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        row_change, col_change = 0, 1
        row, col = 0, 0
        output = []
        while len(output) < COLS*ROWS:
            output.append(matrix[row][col])
            matrix[row][col] = float('inf')
            next_row, next_col = row + row_change, col + col_change
            if (next_row not in range(ROWS)
                or next_col not in range(COLS)
                or matrix[next_row][next_col] == float('inf')):
                if row_change:
                    row_change *= -1
                row_change, col_change = col_change, row_change
            row += row_change
            col += col_change
        return output