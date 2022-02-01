/*
백준 2581번
 */

import java.io.*;

public class PrimeNumber2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int M = Integer.parseInt(br.readLine());
        int N = Integer.parseInt(br.readLine());

        int min = 0, total = 0;
        boolean isPrime, first = true;
        for (int i = M; i <= N; i++) {
            isPrime = true;
            if(i ==1)
                continue;
            for (int j = 2; j < i; j++) {
                if (i % 2 == 0) {
                    isPrime = false;
                    break;
                } else if (i % j == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) {
                total += i;
                if (first) {
                    min = i;
                    first = false;
                }
            }
        }

        if (total == 0) {
            System.out.println(-1);
        } else {
            System.out.println(total);
            System.out.println(min);
        }
    }
}

class PrimeNumber2Solve2 {
    public static boolean[] prime;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int M = Integer.parseInt(br.readLine());
        int N = Integer.parseInt(br.readLine());

        GetPrime(N);
        int min= -1, total = 0;
        Boolean first = true;
        for (int i = M; i <= N; i++) {
            if (!prime[i]) {
                if(min == -1){
                    min= i;
                }
                total += i;
            }
        }
        if (total == 0) {
            System.out.println(-1);
        } else {
            System.out.println(total);
            System.out.println(min);
        }
    }

    public static void GetPrime(int N) {
        prime = new boolean[N+1];

        /*
        true = 소수 아님
        false = 소수
         */
        prime[0] = prime[1] = true;

        for (int i = 2; i <= Math.sqrt(prime.length); i++) {
            if (prime[i]) {
                continue;
            }

            for (int j = i * i; j < prime.length; j += i) {
                prime[j] = true;
            }
        }

    }
}
