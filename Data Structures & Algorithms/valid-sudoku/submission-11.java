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
                if (rows.getOrDefault(row, new HashSet<Character>()).contains(curr)
                || cols.getOrDefault(col, new HashSet<Character>()).contains(curr)
                || squares.getOrDefault(squareKey, new HashSet<Character>()).contains(curr)){
                    return false;
                }
                rows.computeIfAbsent(row, k -> new HashSet<>()).add(curr);
                cols.computeIfAbsent(col, k -> new HashSet<>()).add(curr);
                squares.computeIfAbsent(squareKey, k -> new HashSet<>()).add(curr);
            }
        }
        return true;
    }
}
