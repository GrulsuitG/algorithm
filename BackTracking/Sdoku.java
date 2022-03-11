/*
백준 2580번
 */

import java.util.Scanner;

public class Sdoku {

    static int[][] board = new int[9][9];


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                board[i][j] = sc.nextInt();
            }
        }

        checkBoard(0, 0);

    }

    private static void checkBoard(int row, int col) {
        if (row == 9) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < 9; i++) {
                for (int j = 0; j < 9; j++) {
                    sb.append(board[i][j]).append(' ');
                }
                sb.append('\n');
            }
            System.out.println(sb);
            System.exit(0);
        }
        if (col == 9) {
            checkBoard(row + 1, 0);
        }

        if (board[row][col] == 0) {
            for (int i = 1; i <= 9; i++) {
                if (check(row, col, i)) {
                    board[row][col] = i;
                    checkBoard(row, col + 1);
                }
            }

            board[row][col] = 0;
            return;
        }

        checkBoard(row, col+1);
    }

    private static boolean check(int row, int col, int value) {
        int squareRow = (row / 3) * 3;
        int squareCol = (col / 3) * 3;

        for (int i = squareRow; i < squareRow + 3; i++) {
            for (int j = squareCol; j < squareCol+3; j++) {
                if (board[i][j] == value) {
                    return false;
                }
            }
        }

        for (int i = 0; i < 9; i++) {
            if (board[row][i] == value) {
                return false;
            }
        }

        for (int i = 0; i < 9; i++) {
            if (board[i][col] == value) {
                return false;
            }
        }

        return true;
    }
}

/*
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
 */