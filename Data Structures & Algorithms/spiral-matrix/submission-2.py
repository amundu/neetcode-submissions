class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        visited = set()
        output = []
        row, col = 0, 0
        row_change, col_change = 0, 1

        while len(visited) < ROWS*COLS:
            visited.add((row,col))
            output.append(matrix[row][col])
            next_row, next_col = row + row_change, col + col_change
            if (
                next_row not in range(ROWS) or
                next_col not in range(COLS) or
                (next_row, next_col) in visited 
                ):
                if row_change != 0:
                    row_change *= -1
                row_change, col_change = col_change, row_change
                next_row, next_col = row + row_change, col + col_change
            row, col = next_row, next_col
        return output

