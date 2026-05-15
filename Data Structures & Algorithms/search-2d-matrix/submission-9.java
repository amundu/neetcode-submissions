class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        final int ROWS = matrix.length, COLS = matrix[0].length;
        int low = 0, high = ROWS * COLS-1;

        while (low <= high) {
            int mid = ((high-low)/2)+low;
            int row = mid/COLS, col = mid%COLS;
            if (target < matrix[row][col]){
                high = mid - 1;
            } else if(target > matrix[row][col]){
                low = mid + 1;
            } else {
                return true;
            }
        }
        return false;
    }
}
