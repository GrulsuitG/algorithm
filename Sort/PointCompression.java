/*
백준 18870
 */

import java.io.IOException;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class PointCompression {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] arr = new int[N];
        int[] sorted = new int[N];
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < N; i++) {
            arr[i] = sorted[i] = sc.nextInt();
        }

        Arrays.sort(sorted);

        int rank = 0;
        for (int i : sorted) {
            if (!map.containsKey(i)) {
                map.put(i, rank++);
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i : arr) {
            sb.append(map.get(i)).append(" ");
        }
        System.out.println(sb);
    }
}
