/*
백준 11651번
 */

import java.util.Arrays;
import java.util.Scanner;

public class PointSort2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[][] arr = new int[N][2];

        for (int i = 0; i < N; i++) {
            arr[i][0] = sc.nextInt();
            arr[i][1] = sc.nextInt();
        }

        Arrays.sort(arr, (e1, e2) ->{
            if (e1[1] == e2[1]) {
                return Integer.compare(e1[0], e2[0]);
            } else
                return Integer.compare(e1[1], e2[1]);
        });

        for (int i = 0; i < N; i++) {
            System.out.println(arr[i][0] + " " + arr[i][1]);
        }
    }


}
