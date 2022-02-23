/*
백준 15649번
 */

import java.util.Scanner;
import java.util.Stack;

public class NAndM1 {

    static int[] arr;
    static boolean[] visit;
    static int N;
    static int M;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();

        arr = new int[M];
        visit = new boolean[N];

        BackTracking(0);

        System.out.println(sb);
    }

    static void BackTracking(int depth) {
        if (depth == M) {
            for(int i : arr) {
                sb.append(i).append(' ');
            }
            sb.append('\n');
            return;
        }
        for (int i = 0; i < N; i++) {
            if (!visit[i]) {
                visit[i] = true;
                arr[depth] = i+1;
                BackTracking(depth+1);
                visit[i] = false;
            }
        }

    }

}
