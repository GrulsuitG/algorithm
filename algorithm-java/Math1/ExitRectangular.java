/*
백준 1085번
 */

import java.io.*;

public class ExitRectangular {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");
        int x = Integer.parseInt(input[0]);
        int y = Integer.parseInt(input[1]);
        int w = Integer.parseInt(input[2]);
        int h = Integer.parseInt(input[3]);

        int min1 = Math.min(w - x, x);
        int min2 = Math.min(h - y, y);
        int min = Math.min(min1, min2);
        System.out.println(min);
    }
}
