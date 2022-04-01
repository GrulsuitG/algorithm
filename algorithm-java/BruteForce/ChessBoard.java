/*
백준 1018번
 */


import java.util.Scanner;

public class ChessBoard {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();
        char[][] board = new char[N][M];

        for (int i = 0; i < N; i++) {
            board[i] = sc.next().toCharArray();
        }

        int min = Integer.MAX_VALUE;
        for (int i = 0; i <= (N - 8);  i++) {
            for (int j = 0; j <= (M - 8); j++) {
                char start = board[i][j];
                int pos = (i+j) %2;
                int cnt1 = 0;
                int cnt2 = 0;
                for (int k = i; k < (i + 8); k++) {
                    for (int l = j; l < (j + 8); l++) {
                        if (start == 'W') {
                            if ((k + l) % 2 == pos) {
                                if( board[k][l] != 'W') cnt1++;
                                if(board[k][l] != 'B') cnt2++;
                            } else if ((k + l) % 2 != pos) {
                              if( board[k][l] != 'B') cnt1++;
                              if( board[k][l] != 'W') cnt2++;
                            }
                        }
                        else {
                            if ((k + l) % 2 == pos) {
                                if( board[k][l] != 'B') cnt1++;
                                if( board[k][l] != 'W') cnt2++;
                            } else if ((k + l) % 2 != pos) {
                                if( board[k][l] != 'W') cnt1++;
                                if( board[k][l] != 'B') cnt2++;
                            }
                        }
                    }
                }

                min = Math.min(Math.min(cnt1, cnt2), min);
            }
        }
        System.out.println(min);
    }
}

