/*
백준 1436번
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class NthEndNumber {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int cnt = 0;
        int i;
        for (i = 666; cnt != N; i++) {
            String str = String.valueOf(i);
            if (str.contains("666")) {
                cnt++;
            }
        }
        System.out.println(i-1);
    }
}
