class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        low, high = 0, (ROWS*COLS)-1

        while low <= high:
            mid = low + (high - low) // 2
            row, col = mid // COLS, mid % COLS
            if target < matrix[row][col]:
                high = mid-1
            elif target > matrix[row][col]:
                low = mid+1
            else:
                return True
        return False