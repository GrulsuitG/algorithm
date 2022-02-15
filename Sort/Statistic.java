/*
백준 2108번
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Statistic {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int[] arr = new int[8001];
        double total = 0;
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        int median = 0;
        int mode = 0;
        for (int i = 0; i < N; i++) {
            int temp = Integer.parseInt(br.readLine());
            arr[temp+4000]++;
            total += temp;

            if(max < temp) max = temp;
            if(min > temp) min = temp;
        }

        int count = 0;
        int mode_max = 0;
        boolean flag = false;
        for (int i = min+4000; i <= max+4000; i++) {
            if (arr[i] > 0) {
                if(count < (N+1)/2) {
                    count += arr[i];
                    median = i -4000;
                }
                if (arr[i] > mode_max) {
                    mode = i-4000;
                    mode_max = arr[i];
                    flag = true;
                } else if (arr[i] == mode_max && flag) {
                    mode = i-4000;
                    flag = false;
                }
            }
        }

        System.out.println(Math.round(total / N));
        System.out.println(median);
        System.out.println(mode);
        System.out.println(max-min);
    }
}
