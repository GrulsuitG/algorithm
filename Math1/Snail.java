/*
백준 2869
시간을 최소화 하기 위해 bufferedWriter 사용
 */

import java.io.*;

public class Snail {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] str = br.readLine().split(" ");
        double a = Integer.parseInt(str[0]);
        double b = Integer.parseInt(str[1]);
        double v = Integer.parseInt(str[2]);
        int height = 0;
        double day = Math.ceil((v - a) / (a - b)) + 1;
        bw.write(String.valueOf((int)day));
        bw.flush();
    }
}
