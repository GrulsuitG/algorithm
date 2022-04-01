/*
백준 9663번
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class NQueen {

    static int[] board;
    static int N;
    static int count = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        board = new int[N];

        DFS(0);
        System.out.println(count);
    }

    static void DFS(int depth) {
        if (depth == N) {
            count++;
            return;
        }
        for (int i = 0; i < N; i++) {
            board[depth] = i;
            boolean isDup = false;
            for (int j = 0; j < depth; j++) {
                if (board[j] == i || board[j] == i - depth + j || board[j] == i + depth - j) {
                    isDup = true;
                    break;
                }
            }

            if (!isDup) {
                DFS(depth + 1);
            }

        }
    }
}
