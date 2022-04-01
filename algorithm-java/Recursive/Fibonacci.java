/*
백준 10870번
 */

import java.io.*;

public class Fibonacci {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int res = Calc(n);
        System.out.println(res);
    }

    private static int Calc(int n) {
        if (n == 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        } else {
            return Calc(n-1) + Calc(n-2);
        }

    }
}
