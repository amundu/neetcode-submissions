class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        low, high = 0, ROWS*COLS-1
    
        while low <= high:
            mid = ((high-low)//2)+low
            n = matrix[mid//COLS][mid%COLS]
            if n < target:
                low = mid + 1
            elif n > target:
                high = mid -1
            else:
                return True

        return False