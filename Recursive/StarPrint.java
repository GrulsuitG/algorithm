/*
백준 2447번
 */

import java.io.*;

public class StarPrint {

    static char[][] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        arr = new char[n][n];

        makeStar(0, 0, n, false);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                sb.append(arr[i][j]);
            }
            sb.append('\n');
        }
        System.out.println(sb);
    }

    public static void makeStar(int x, int y, int N, boolean Empty) {
        if (Empty) {
            for (int i = x; i < x + N; i++) {
                for (int j = y; j < y + N; j++) {
                    arr[i][j] = ' ';
                }
            }
        } else if (N == 1) {
            arr[x][y] = '*';
        } else {
            int size = N/3;
            int count = 0;
            for (int i = x; i < x + N; i += size) {
                for (int j = y; j < y + N; j+=size) {
                    count++;
                    makeStar(i, j, size, count == 5);
                }
            }
        }
    }

}

