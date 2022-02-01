/*
백준 1978반
 */

import java.io.*;

public class PrimeNumber {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int num = Integer.parseInt(br.readLine());
        String[] prime = br.readLine().split(" ");
        int total = 0;
        for (int i = 0; i < num; i++) {
            if (isPrime(Integer.parseInt(prime[i]))) {
                total++;
            }
        }
        System.out.println(total);
    }

    static Boolean isPrime(int n) {
        if(n == 1)
            return false;
        for (int i = 2; i < n; i++) {
            if(n % i == 0)
                return false;
        }
        return true;
    }
}
