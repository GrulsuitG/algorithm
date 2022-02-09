/*
백준 11729번
 */

import java.io.*;

public class Hanoi {

    public static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        System.out.println((int)Math.pow(2,n)-1);
        move(n, 1, 3);
        System.out.println(sb);
    }

    public static void move(int n, int cur, int target) {
        if (n == 1) {
            sb.append(cur).append(" ").append(target).append('\n');
        } else {
            int other = target ^ cur;
            move(n-1, cur, other);
            move(1, cur, target);
            move(n - 1, other, target);


        }
    }
}
