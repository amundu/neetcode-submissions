class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        n = ROWS * COLS

        low, high = 0, n-1

        while low <= high:
            mid = low + (high-low)//2
            row, col = mid // COLS, mid%COLS
            if matrix[row][col] < target:
                low = mid + 1
            elif matrix[row][col] > target:
                high = mid -1
            else:
                return True
        return False