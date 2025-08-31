class Solution {
    public void solveSudoku(char[][] board) {
        solve(board);
    }

    private boolean solve(char[][] board) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') {
                    for (char guess = '1'; guess <= '9'; guess++) {
                        if (isValid(board, i, j, guess)) {
                            board[i][j] = guess;

                            if (solve(board)) {
                                return true;
                            } else {
                                board[i][j] = '.';
                            }
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }

    private boolean isValid(char[][] board, int row, int col, char guess) {
        for (int i = 0; i < 9; i++) {
            if (board[row][i] == guess) {
                return false;
            }
            if (board[i][col] == guess) {
                return false;
            }
            if (board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] == guess) {
                return false;
            }
        }
        return true;
    }
}