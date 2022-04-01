/*
백준 1929번
 */

import java.io.*;

public class GetPrimeNumber {
    public static boolean[] prime;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] num = br.readLine().split(" ");
        prime = new boolean[Integer.parseInt(num[1])+1];
        GetPrime();

        for (int i = Integer.parseInt(num[0]); i <= Integer.parseInt(num[1]); i++) {
            if (!prime[i]) {
                System.out.println(i);
            }
        }

    }

    public static void GetPrime() {
        prime[0] = prime[1] = true;

        for (int i = 2; i < Math.sqrt(prime.length); i++) {
            if (prime[i]) {
                continue;
            }
            for (int j = i * i; j < prime.length; j += i) {
                prime[j] = true;
            }
        }

    }
}
