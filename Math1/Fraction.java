/*
백준 1193
 */

import java.io.*;

public class Fraction {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int num = Integer.parseInt(br.readLine());
        int n = 1;

        while (num > (n * n + n) / 2) {
            n++;
        }
        int an = (n * n + n) / 2;
        int order = an - num;

        if (n % 2 == 0)
            System.out.println((n - order) + "/" + (1 + order));
        else
            System.out.println((1 + order) + "/" + (n - order));

    }
}
