/*
백준 10989번
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class SortNumber3 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[10001];
        for (int i = 0; i < N; i++) {
            arr[Integer.parseInt(br.readLine())]++;
        }
        StringBuilder sb = new StringBuilder();
        for(int i =1; i <= 10000; i++) {
            int time = arr[i];
            for (int j = 0; j < time; j++) {
                sb.append(i).append('\n');
            }
        }
        System.out.println(sb);
    }
}
