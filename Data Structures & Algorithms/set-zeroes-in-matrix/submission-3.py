class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rows_zero, cols_zero = [1]*ROWS, [1]*COLS

        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] != 0:
                    continue
                rows_zero[row] = 0
                cols_zero[col] = 0
        
        for row in range(ROWS):
            for col in range(COLS):
                if rows_zero[row] == 0 or cols_zero[col] == 0:
                    matrix[row][col] = 0
                
        