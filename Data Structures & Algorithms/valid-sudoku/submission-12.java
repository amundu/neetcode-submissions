class Solution {
    public boolean isValidSudoku(char[][] board) {
        final int ROWS = board.length, COLS = board[0].length;

        Map<Integer, Set<Character>> rows = new HashMap();
        Map<Integer, Set<Character>> cols = new HashMap();
        Map<String, Set<Character>> squares = new HashMap();

        for (int row = 0; row < ROWS; row++){
            for (int col = 0; col < COLS; col++){
                char curr = board[row][col];
                if (curr == '.'){
                    continue;
                }
                String squareKey = (row/3) + "," + (col/3);
                if (rows.computeIfAbsent(row, k -> new HashSet<>()).contains(curr)
                || cols.computeIfAbsent(col, k -> new HashSet<>()).contains(curr)
                || squares.computeIfAbsent(squareKey, k -> new HashSet<>()).contains(curr)){
                    return false;
                }
                rows.get(row).add(curr);
                cols.get(col).add(curr);
                squares.get(squareKey).add(curr);
            }
        }
        return true;
    }
}
