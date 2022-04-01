/*
백준 2798번
 */

import java.util.ArrayList;
import java.util.Scanner;

public class BlackJack {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();
        ArrayList<Integer> arr = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            arr.add(sc.nextInt());
        }

        int max = 0;
        for (int i = 0; i < N-2; i++) {
            int one = arr.get(i);
            for (int j = i + 1; j < N-1; j++) {
                int two = arr.get(j);
                for (int k = j + 1; k < N; k++) {
                    int three = arr.get(k);
                    int sum = one + two + three;
                    if (sum == M) {
                        max = M;
                    } else {
                        if (sum < M && M - sum < M - max) {
                            max = sum;
                        }
                    }
                }
            }
        }
        System.out.println(max);
    }
}
