/*
백준 4948번
 */

import java.io.*;

public class ChebyshevTheorem {
    public static boolean[] prime;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num, cnt;
        while ((num = Integer.parseInt(br.readLine())) != 0) {
            GetPrime(num*2);
            cnt = 0;
            for (int i = num+1; i <= num * 2; i++) {
                if (!prime[i]) {
                    cnt++;
                }
            }
            System.out.println(cnt);
        }
    }
    public static void GetPrime(int n) {
        prime = new boolean[n+1];
        prime[0] = prime[1] = true;

        for (int i = 2; i <= Math.sqrt(prime.length); i++) {
            if (prime[i])
                continue;
            for (int j = i * i; j < prime.length; j += i) {
                prime[j] = true;
            }
        }
    }
}
