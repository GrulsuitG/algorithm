/*
백준 15650번

 */


import java.util.Scanner;

public class NAndM2 {

    static int N;
    static int M;

    static int[] arr;

    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();

        arr = new int[M];

        Backtracking(0, 0);

        System.out.println(sb);
    }

    static void Backtracking(int depth, int num) {
        if (depth == M) {
            for (int i = 0; i < M; i++) {
                sb.append(arr[i]).append(' ');
            }
            sb.append('\n');
            return;
        }

        for (int i = num; i < N; i++) {
            arr[depth] = i+1;
            Backtracking(depth+1, i+1);
        }
    }

}
