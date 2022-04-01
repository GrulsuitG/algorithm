/*
백준 2231번
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class DigitGenerator {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int i;
        for (i = 1; i < N; i++) {
            int res = digitGenerator(i);
            if (res == N) {
                System.out.println(i);
                break;
            }
        }

        if (i == N) {
            System.out.println(0);
        }
    }

    public static int digitGenerator(int n) {
        ArrayList<Integer> arr = new ArrayList<>();

        int sum = n;
        while (n > 0) {
            sum += n %10;
            n /= 10;
        }
        return sum;
    }
}
