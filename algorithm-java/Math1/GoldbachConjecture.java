/*
백준 9020번
 */

import java.io.*;

public class GoldbachConjecture {
    public static boolean[] prime;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int caseNum = Integer.parseInt(br.readLine());
        for (int i = 0; i < caseNum; i++) {
            int num = Integer.parseInt(br.readLine());
            GetPrime(num);
            int num1 = num / 2;
            int num2 = 0;
            while (num1 >1) {
                if (!prime[num1]) {
                    num2 = num - num1;
                    if(!prime[num2])
                        break;
                }
                num1--;
            }
            System.out.println(num1+ " " + num2);
        }
    }

    private static void GetPrime(int n) {
        prime = new boolean[n+1];
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
