/*
백준 10250번
 */

import java.io.*;

public class ACMHotel {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int testCase = Integer.parseInt(br.readLine());

        for(int i = 0; i<testCase; i++){
            String[] str = br.readLine().split(" ");
            int h = Integer.parseInt(str[0]);
            int w = Integer.parseInt(str[1]);
            int n = Integer.parseInt(str[2]);

            String floor = String.valueOf(n % h == 0 ? h : n%h);
            String unit = String.valueOf((int)Math.ceil((double) n / h));
            unit = unit.length() < 2 ? "0".concat(unit) : unit;

            System.out.println(floor + unit);
        }
    }
}
